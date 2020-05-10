package shangji4;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class test {
    private static page [] page=new page[32];//每个进程享有32个页面
    private static pageFrame[] pageFrames=new pageFrame[4];//有4个页框
    private static Queue<page> pageQueue=new LinkedList<page>();
    //private static Queue<Integer> cmd=new LinkedList<Integer>();
    private static int [] cmd;
    private static int [] pageOrder;
    private static int indexcmd=0;
    private static int hit=0;
    private static int indexFrame=0;
    private static int cmdNum=100;
    private static int range=100;//生成指令的范围
    //private static int miss=0;
    public static void main(String[] args){
        initPage(10);
        initPageFrame();
        initCMD();
        turnToPageQueue();
        run();

    }

    public static void run(){
        while(indexcmd<cmdNum){
//            int num=cmd[indexcmd++];
            int pageNum=pageOrder[indexcmd++];
            //更新页面的队列
            pageQueue.remove(page[pageNum]);
            pageQueue.add(page[pageNum]);
            int tmp=judgeExit(pageNum);
            if(indexFrame<4){
                if(tmp!=-1){//已存在于物理页中
                    continue;
                }
                pageFrames[indexFrame++].setPageNum(pageNum);//第一次分配四个页框
            }
            else {


                if(tmp==-1){//不在内存中
                    //按照某一个算法排除一个页后插入当前页
                    LRU(page[pageNum]);

                }
                else{ //已存在内存中 命中
                    hit++;
                    //其他等待次数加一
                    addWait(tmp);
                    continue;
                }

            }

        }

        System.out.println("命中次数:"+hit);


    }
    //将指令序列转换为页地址流
    public static int[] turnToPageQueue(){
        pageOrder=new int[cmdNum];

        for(int i=0;i<cmdNum;i++){
            pageOrder[i]=cmd[i]/10;
        }
        return pageOrder;
    }
    //初始化num个页面
    public static void initPage(int num){
        int indexPage=0;
        int index=0;
        int[] cmd=new int[10];
        for(int i=0;i<num;i++){
            page[indexPage]=new page(indexPage++);
        }
    }

    //
    public static void initPageFrame(){
        for(int i=0;i<4;i++){
            pageFrames[i]=new pageFrame(i);
        }
    }
    //随机生成范围在320内的命令
    public static void initCMD(){
        Random random=new Random();
        cmd=new int[cmdNum];
        for(int i=0;i<cmdNum;i++){
            cmd[i]=(random.nextInt(100));
        }
    }
    //该物理页中是否拥有该页号
    public static int judgeExit(int pageNum) {
        //int cmdNum=cmd.poll();
        for (int i = 0; i < 4; i++) {
            if (pageFrames[i].getPageNum() == pageNum) {
                return i;
            }
        }
        return -1;
    }
    public static int findFrameNum(page page){
        for(int i=0;i<4;i++){
            if(pageFrames[i].getPageNum()==page.getPageNum()){
                return i;
            }
        }
        return -1;
    }
    //先进先出
    public static void FIFO(page curPage){
        //找到要移除的页所对应的页框
        page page=pageQueue.poll();
        int i=findFrameNum(page);
        if(i==-1){
            System.out.println("fail to find this page in frame!");
        }
        else{
            //移除该页 转为当前页面
            pageFrames[i].setPageNum(curPage.getPageNum());
        }
    }

    //LRU  移除最久未使用的页面
    public static int findMovedFrameNumLRU(){
        int max=pageFrames[0].getWait();
        int num=0;
        for(int i=1;i<4;i++){
            if(pageFrames[i].getWait()>max){
                max=pageFrames[i].getWait();
                num=i;
            }
        }
        return num;
    }
    public static void LRU(page curPage){
        int n=findMovedFrameNumLRU();
        addWait(n);
        pageFrames[n].setPageNum(curPage.getPageNum());
        pageFrames[n].setWait(0);
    }

    public static void addWait(int except){
        for(int i=0;i<4;i++){
            if(i!=except){
                pageFrames[i].addWait();
            }
        }
    }
    //OPT  移除当前页框表中在未来最晚使用的页面
    public static int findMovedFrameNumOPT(){
        int[][] frameNums=new int[4][2];//[][0]记录页面编号  [][1]记录等待次数
        for(int i=0;i<4;i++){
            frameNums[i][0]=pageFrames[i].getPageNum();
        }
        for(int i=indexcmd;i<cmdNum;i++){
            //从当前Index往后找  若页数相同 [][1]+1
            int numPage=cmd[i]/10;
            int tmp=-1;
            if(numPage==frameNums[0][0]){
                tmp=0;
            }
            else if(numPage==frameNums[1][0]){
                tmp=1;
            }
            else if(numPage==frameNums[2][0]){
                tmp=2;
            }
            else if(numPage==frameNums[3][0]){
                tmp=3;
            }
            if(tmp==-1){
                continue;//四个都没出现 都加一相当于都不加
            }
            else{
                //出现一个 其余三个等待次数加一
                for(int j=0;j<4;j++){
                    if(tmp!=j)
                        frameNums[j][1]++;
                }
            }

        }
        //寻找最大的等待时间  返回该页框号
        int max=frameNums[0][0];
        int num=0;
        for(int i=1;i<4;i++){
            if(frameNums[i][1]>max){
                max=frameNums[i][1];
                num=i;
            }
        }
        return num;
    }
    public static void OPT(page curPage){
        int frameNum=findMovedFrameNumOPT();
        pageFrames[frameNum].setPageNum(curPage.getPageNum());
    }

//    public static void initgrah(){
//        JFrame jf=new JFrame("运行窗口");
//        jf.setSize(400,400);
//        jf.setLocationRelativeTo(null);
//        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
//
//        JPanel panel=new JPanel(new BorderLayout());
//
//        jf.setContentPane(panel);
//
//
//    }

}
