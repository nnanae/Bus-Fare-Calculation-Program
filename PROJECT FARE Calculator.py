from tkinter import*   #Import Tkinter
from tkinter import ttk
from tkinter import messagebox

p = Tk()
p.configure(background="#CCFFFF")
p.title('FARE CALCULATOR')
p.minsize(450,350)
p.maxsize(450,350)

lb = Label(p,text="WELCOME TO FARE CALCULATOR",font="20",background="pink")
lb.place(x=20,y=30)
lb.pack()

a = Label(p,text=" สถานีต้นทาง = ",font="20",background="light yellow")
a.pack()
a.place(x="20",y="30")

a2 = Label(p,text=" สถานีปลายทาง = ",font="20",background="light yellow")
a2.pack()
a2.place(x="20",y="70")

f11=['ตลาดเจริญผลวัฒนา','ท่ารถปทุมธานี','โรงเรียนปทุมวิไล','หมู่บ้านปทุมทอง','ชุมชนสมประสงค์','หมู่บ้านปทุมวิลเลจ','หมู่บ้านทรัพย์กานดา','ตรงข้ามบิ๊กซีปทุมธานี','หมู่บ้านทิพย์มณี',\
     'ซอยเทศบาล5','ตรงข้ามโรงแรมดาร์ลิ่งอินน์','ตรงข้ามซอยวัดไพร่ฟ้า','ตรงข้ามหมู่บ้านมณฑลาภ','ตรงข้ามหมู่บ้านไพฑูรย์แกรนด์วิลล์','หมู่บ้านธรรมสุธีร์','หมู่บ้านพูลศรี','ตรงข้ามบ้านเอื้ออาทร บางคูวัด',\
     'ตรงข้ามหมู่บ้านภัทรนิเวศน์','หมู่บ้านกฤษติญา','ตรงข้ามวัดบางนางบุญ','ตรงข้ามโรงเรียนวัดบางนางบุญ','ตรงข้ามซอยใจเอื้อ','ตรงข้ามชุมชนสายบัว','แยกสวนสมเด็จ(ฝั่งติวานนท์)','หมู่บ้านมิตรประชา',\
     'ตรงข้ามโรงเรียนกองทัพบกอุปถัมภ์ ช่างกล ขส.ทบ.','ถนนบอนด์สตรีท','ซอยติวานนท์-ปากเกร็ด34','ตรงข้ามโรงเรียนอัมพรไพศาล','ตรงข้ามหมู่บ้านลานทอง',"ซอยหมู่บ้านสหกรณ์ฯ3",'หมู่บ้านปากเกร็ดวิลเล็จ',\
     "ตรงข้ามรพ.กรุงไทย","โรงเรียนสวนกุหลาบ นนทบุรี","ตรงข้ามเคหะนนทบุรี(ฝั่งติวานนท์)","หลังแยกปากเกร็ด","หมู่บ้านเกื้อกูลนิเวศน์","ตรงข้ามโรงเรียนศรีสังวาลย์","วัดชลประทานรังสฤษฎ์",'โรงเรียนชลประทานวิทยา',\
     "ศูนย์ปฎิบัติการจัดระเบียบนักเรียน นนทบุรี","โรงเรียนชลประทานสงเคราะห์","ถนนสามัคคี","ซอยติวานนท์ 50/2","ตรงข้ามโตชิบา","ซอยติวานนท์ 44","ตรงข้ามกรมพลาธิการทหารบก" ,'ซฮยทานสัมฤทธิ์',\
     "โรงเรียนนนทบุรีพิทยาคม","กฟน.นนทบุรี","ตรงข้ามสำนักงานขนส่งจังหวัดนนทบุรี","สถาบันโรคทรวงอก","ซอยติวานนท์ 18","เอลิสคอนโดมิเนียม ติวานนท์","ตรงข้ามถนนเรวดี","ซอยติวานนท์ 8",'กระทรวงสาธารณสุข',\
     "ตรงข้ามบิ๊กซีติวานนท์","โรงเรียนวัดลานนาบุญ","วัดลานนาบุญ","ซอยประชาราษฎร์ 3","หมู่บ้าน ซ.รุ่งเรือง 4","ตรงข้ามวัดทินกรนิมิต","ซอยประชาราษฎร์ 11","เมเจอร์นนทบุรี","แยกเลี่ยงเมืองนนทบุรี","โรงเรียนการัญศึกษา",\
     'แยกพระราม 5','วัดกำแพง(นนทบุรี)','ซอยพิบูลสงคราม 18','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์','ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านบ้านพิบูลย์','มาสต้า พระราม 7','มจพ.','สวนสะพานพระราม 7',\
     'ตรงข้ามวัดสร้อยทอง','ตลาดศรีเขมา','โรงเรียนกุลวรรณศึกษา','ก่อนแยกบางโพ','สถานีดับเพลิงบางโพ','วัดประดู่ธรรมาธิปัตย์','แยกเกียกกาย','กองพันทหารม้าที่ 4','สุพรีมสามเสน','ตรงข้ามโรงเรียนราชินีบน','หลังแยกศรีย่าน','ตรงข้ามวชิรพยาบาล',\
     'ม.ราชภัฎสวนสุนันทา(ฝั่งสามเสน)','ตรงข้ามโณงเรียนเซนต์คาเบรียล','ตรงข้ามหอสมุดแห่งชาติ','ตรงข้าม มทร.พระนคร ศูนย์เทเวศร์','ตลาดรวมยาง','วัดอินทรวิหาร','วัดใหม่อมตรส','ตรงข้ามสำนักงานเขตพระนคร','ถนนข้าวสาร','หอศิลป์เจ้าฟ้า',\
     'ตรงข้ามโรงละครแห่งชาติ','สนามหลวง(ตรงข้ามม.ธรรมศาสตร์)','สนามหลวง(ตรงข้ามวัดมหาธาตุ)']
f12=['อู่ไทรม้า','โรงเรียนป่าไม้อุทิศ 9','ตรงข้ามซอยท่าอิฐ','ซอยบางรักน้อย 2','ตรงข้ามหมู่บ้านประดับดาว','หมู่บ้านคาซ่าแกรนด์ รัตนาธิเบศร์-ราชพฤกษ์','หมู่บ้านประดับดาว','หมู่บ้านคาซ่าวิลล์ ราชพฤกษ์-รัตนาธิเบศร์','หมู่บ้านลภาวัน 17',\
     'ตรงข้ามหมู่บ้านทานตะวัน ท่าอิฐ','หมู่บ้านมณียา','ตรงข้ามหมู่บ้านนันทนา','ตรงข้ามอู่ท่าอิฐ','หลังแยกท่าอิฐ-ไทรม้า','หมู่บ้านซื่อตรงการ์เด้น','MRT ไทรม้า','ริชพาร์ค','หมู่บ้านนนท์ณิชา','หลังแยกพระนั่งเกล้า','แอสปาย รัตนาธิเบศร์',\
     'เซนทรัลรัตนาธิเบศร์','ตรงข้ามซอยวัดสมรโกฎิ','บิ๊กซีรัตนาธิเบศร์','ซอยวัดสมรโกฎิ','ตรงข้ามเซนทรัลรัตนาธิเบศร์','หลังแยกเรวดี-เลี่ยงเมืองนนทบุรี','หมู่บ้านเรวดี 3','ตรงข้ามวัดทินกรนิมิต','ซอยประชาราษฎร์ 11','ท่าน้ำนนทบุรี','เมเจอร์นนทบุรี',\
     'แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกำแพง','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์','ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์',\
     'มาสด้า พระราม7','มจพ.','สวนสะพานพระราม 7','ซอยจรัญสนิทวงศ์ 96/2','วิทยาลัยเทคโนโลยีพระรามหก','รพ.ยันฮ๊','MRT บางอ้อ','โรงเรียนบางอ้อศึกษา','ตรงข้ามวัดสามัคคีสุทธาวาส','ตรงข้ามสำนักงานเขตบางพลัด','วัดอาวุธวิกสิตาราม',\
     'โลตัสจรัญสนิทวงศ์','วัดเทพากร','ตรงข้ามโรงเรียนพิมลวิทย์','วัดเปาโรหิตย์','โรงเรียนพณิชยการสยาม','ตลาดพงษ์ทรัพย์','MRT บางยี่ขัน(ทางออก 4)','ซอยจรัญสนิทวงศ์ 40','พาต้าปิ่่นเกล้า','ก่อนสะพานปิ่นเกล้า','กองสลาก(จุดที่ 1)',\
     'แยกคอกวัว','ศาลกีฎา','วัดพระแก้ว','ท่ามหาราช','ท่าพระจันทร์','สนามหลวง(ตรงข้ามวัดมหาธาตุ)']
f13=['ตรงข้ามสำนักงานประกันสังคม','ตรงข้ามสำนักงานก.พ.นนทบุรี','กระทรวงสาธารณสุข','ตรงข้ามบิ๊กซีติวานนท์'\
     ,'โรงเรียนวัดลานนาบุญ','วัดลานนาบุญ','ซอยประชาราษฎ์ 3','หมู่บ้าน ซ.รุ่งเรือง','ตรงข้ามวัดทินกรนิมิต','ซอยประชาราษฎ์ 11',\
     'ท่าน้ำนนทบุรี','เมเจอร์นนทบุรี','แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกแพงนนทบุรี','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์',\
     'ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์','มาสด้า พระราม7','มจพ.','แยกพิบุลสงคราม','ตรงข้ามวัดเสาหิน','นาดาวเพลส','วัดน้อย','ซอยวัดหลวง','ตรงข้ามบิ๊กซีวงศ์สว่าง','ซอยกรุงเทพ-นนทบุรี 48','ซอยกรุงเทพ-นนทบุรี 44','โรงเรียนพิริยะโยธิน',\
     'ตรงข้ามตลาดบางซ๋อน','MRT บางช่อน(ทางออก 2)','ไปรษณ๊ย์บางซื่อ','ตรงข้าม สน.เตาปูน','ซอยกรุงเทพ-นนทบุรี 20','ซอยกรุงเทพ-นนทบุรี 12','ก่อนแยกเตาปูน','ตลาดเตาปูน','สถานีบางซื่อ','เตาปูนแมนชั่น','โรงเรียนช่างอากาศบำรุง',\
     'ก่อนแยกสะพานแดง(ขาเข้า)','กรมช่างอากาศ','ตรงข้ามส.ป.ท.ประดิพัทธิ์','โรงแรมกานด์มณีพาเลซ','โรงแรมประดิพันธิ์','ซอยประดิพัทธิ์ 21','สน.บางซื่อ','BTS อารีย์(ทางออก 4)','ตรงข้ามซอยราชครู','ซอยพหลโยธิน 2',\
     'BTS สนามเป้า(ทางออก 4)','สถานีวิทยุโทรทัศน์กองทัพบช่อง 5','ตรงข้ามซอยลือชา','อนุสาวรีย์ชัยสมรภูมิ(เกาะราชวิถี)','รพ.เด็ก','โรงเรียนสอนคนตาบอดกรุงเทพ','องค์การเภสัชกรรม','กระทรวงอุตสาหกรรม','รพ.สงฆ์']
f14=['ท่าเรือปากเกร็ด','ตลาดปากเกร็ด','หมู่บ้านบูรพาวิลล่า','ตรงข้ามเมเจอร์ปากเกร็ด','หลังแยกปากกร็ด','หมู่บ้านเกื้อกูลนิเวศน์','ตรงข้ามโรงเรียนศรีสังวาลย์','วัดชลประทานรังสฤษฎ์','โรงเรียยนชลประทานวิทยา','ศูนย์ปฏิบัติการจัดระเบียบนักเรียน นนทบุรี',\
     'โรงเรียนชลประทานสงเคราะห์','ถนนสามัคคี','ซอยติวานนท์ 50/2','ตรงข้ามโตชิบา','ซอยติวานนท์ 44','ตรงข้ามกรมพลาธิการทหารบก','ซอยทานสัมฤทธิ์','โรงเรียนนนทบุรีพิทยาคม','กฟน.นนทบุรี','ตรงข้ามสำนักงานขนส่งจังหวัดนนทบุรี',\
     'สถาบันทรวงอก','ซอยติวานนท์ 18','เอลิสคอนโดมิเนียม ติวานนท์','ตรงข้ามถนนเรวดี','ซอยติวานนท์ 8','กระทรวงสาธารณสุข','ตรงข้ามบิ๊กซีติวานนท์','โรงเรียนวัดลานนาบุญ','วัดลานนาบุญ','ซอยประชาราษฎ์ 3','หมู่บ้าน ซ.รุ่งเรือง 4',\
     'ตรงข้ามวัดทินกรนิมิต','ซอยประชาราษฎ์ 11','เมเจอร์นนทบุรี','แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกำแพงนนทบุรี','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข',\
     'หมู่บ้านพิบูลย์พาร์ควิลล์','ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์','มาสด้า พระราม7','มจพ.''สวนสะพานพระราม 7','ตรงข้ามวัดสร้อยทอง','ตลาดศรีเขมา','โรงเรียนกุลวรรณศึกษา','ก่อนแยกบางโพ','สถานีดับเพลิงบางโพ','วัดประดู่ธรรมาธิปัตย์',\
     'แยกเกียกกาย','กองพันทหารม้าที่ 4','สุพรีมสามเสน','ตรงข้ามโรงเรียนราชินีบน','หลังแยกศรีย่าน','ตรงข้ามวชิรพยาบาล','ม.ราชภัฎสวนสุนันทา(ฝั่งสามเสน)','ตรงข้ามโณงเรียนเซนต์คาเบรียล','ตรงข้ามหอสมุดแห่งชาติ','ตรงข้าม มทร.พระนคร ศูนย์เทเวศร์',\
     'ตลาดรวมยาง','วัดอินทรวิหาร','วัดใหม่อมตรส''ตรงข้ามสำนักงานเขตพระนคร','ถนนข้าวสาร','กองสลาก(จุดที่ 1)','แยกคอกวัว','ศาลกีฎา','ศาลหลังเมือง','กระทรวงกลาโหม','วัดโพธิ์']
f15=['ท่าน้ำนนทบุรี','เมเจอร์นนทบุรี','แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกำแพงนนทบุรี','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์',\
     'ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์','มาสด้า พระราม7','มจพ.','แยกพิบูลสงคราม','ตรงข้ามวัดเสาหิน','นาดาวเพลส','วัดน้อย','ซอยวัดหลวง','ซอยวงศืสว่าง 23','ตรงข้ามบิ๊กซีวงศ์สว่าง','หลังแยกวงศ์สว่าง',\
     'ตรงข้ามกรมยุทธบริการทหาร','หมู่บ้านโซล รัชดาภิเษก 68','ก่อนแยกประชานุกูล','ซอยรัชดาภิเษก 60','ซอยรัชดาภิเษก 58','ตรงข้ามเอสซีบี ปาร์ค พลาซ่า','เมเจอร์รัชโยธิน','หลังแยกเสนานิคม','ตลาดอมรพันธ์',\
     'ม.เกษตรศาสตร์(ประตูพหลโยธิน)','กรมส่งเสริมการเกษตร','สำนักงานคณะกรรมการวิจัยแห่งชาติ','กรมป่าไม้','ไปรษณีย์จตุจักร','ตรงข้ามโรงเรียนสารวิทยา','ตรงข้าม ม.ศรีปทุม','ตรงข้ามโรงเรียนสารวิทยา','ตรงข้าม ม.ศรีปทุม'\
     'โรงเรียนบางบัว','หมู่บ้านถาวิลวิลล่าบางบัว 1','บ้านบางเขน','ซอยพหลโยธิน 49/2','ก่อนอู่บางเขน','อู่บางเขน']
f16=['ท่าน้ำนนทบุรี','เมเจอร์นนทบุรี','แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกำแพงนนทบุรี','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์',\
     'ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์','มาสด้า พระราม7','มจพ.','สวนสะพานพระราม7','ตรงข้ามวัดสร้อยทอง','ตลาดศรีเขามา','โรงเรียนกุลวรรณศึกษา','ก่อนแยกบางโพ','สถานีดับเพลิงบางโพ','วัดประดู่ธรรมาธิปัตย์','แยกเกียกกาย(ขาเข้า)',\
     'ปตอ.','ตรงข้ามกรมทหารม้าที่ 1','โรงเรียนทหารสรรพาวุธ','ตรงข้ามกรมทหารสื่อสาร','กรมช่างอากาศ','ตรงข้ามกรมทหารปืนใหญ่ที่ 1','ไปรษณีย์ประดิพัทธ์','ตรงข้าม ส.ป.ก.ประดิพัทธิ์','โรงแรมกานต์มณีพาเลช','โรงแรมประดิพัทธิ์',\
     'ซอยประดิพัทธิ์ 21','หลังแยกสะพานควาย','โรงแรมสุดาพาเลช','ซอยอินทามระ 21','แยกสุทธิสาร(ฝั่งอินทามระ ขาออก)','ตรงข้ามตลาดสุทธิสาร','ตรงข้ามซอยอินทามระ28','ซอยอินทามระ 45','ไปรษณีย์สุทธิสาร','ซอยอินทามระ 59',\
     'ตรงข้ามซอยประชาสงค์เคราะห์ 47','ตลาดห้วยขวาง','หอนาฬิกาห้วยขวาง','ตรงข้ามทีวีซีคอนโดมิเนียม 2','ตรงข้ามวัดพรมวงศาราม','ดีดีทาวเวอร์','ซอยประชาสงเคราะห์ 16','โรงเรียนพร้อมพรรณวิทยา','ตรงข้ามศูนย์บริการสาธารณสุข 4',\
     'ตรงข้ามโรงเรียนวิชูทิศ','ซอยมิตรไมตรี 3','ท่ารถศาลาว่าการ กทม.2']
f17=['ท่าน้ำนนทบุรี','เมเจอร์นนทบุรี','แยกเลี่ยงเมืองนนทบุรี','โรงเรียนการัญศึกษา','แยกพระราม 5','วัดกำแพงนนทบุรี','ซอยพิบูลสงคราม 18','หมู่บ้านวิสต้า วันเอทโอ','หมู่บ้านพิบูลย์การ์เด้นวิลล์','ซอยแสนสุข','หมู่บ้านพิบูลย์พาร์ควิลล์',\
     'ตรงข้ามโรงเรียนสตรีนนทบุรี','หมู่บ้านพิบูลย์','มาสด้า พระราม7','มจพ.','สวนสะพานพระราม7','ตรงข้ามวัดสร้อยทอง','ตลาดศรีเขามา','โรงเรียนกุลวรรณศึกษา','ก่อนแยกบางโพ','สถานีดับเพลิงบางโพ','วัดประดู่ธรรมาธิปัตย์','แยกเกียกกาย(ขาเข้า)'\
     'กองพันทหารม้าที่ 4','สุพรีมสามเสน','ตรงข้ามโรงเรียนราชินีบน','หลังแยกศรีย่าน','ตรงข้ามวชิรพยาบาล','ม.ราชภัฎสวนสุนันทา(ฝั่งสามเสน)','ตรงข้ามโรงเรียนเซนต์คาเบรียล','ตรงข้ามหอสมุดแห่งชาติ','ตรงข้าม มทร.พระนคร ศูนย์เทเวศร์'\
     'ตลาดรวมยาง','วัดอินทรวิหาร','วัดใหม่อมตรส','ตรงข้ามสำนักงานเขตพระนคร','ถนนข้าวสาร','หอศิลปเจ้าฟ้า','ตรงข้ามโรงละครแห่งชาติ','สนามหลวง(ตรงข้าม ม.ธรรมศาสตร์)','สนามหลวงวัดมหาธาตุ','กระทรวงกลาโหม','ท่ารถคลองคูเมืองเดิม']

play=StringVar()
end=StringVar()
abc=IntVar()

dog=Radiobutton(p,text='สีชมพู',variable=abc,value=1,state="disabled")
dog.pack()
dog.place(x='20',y='150')
god=Radiobutton(p,text='สีส้ม',variable=abc,value=2,state="disabled")
god.pack()
god.place(x='80',y='150')
doo=Radiobutton(p,text='รถแอร์สีเหลือง',variable=abc,value=3,state="disabled")
doo.pack()
doo.place(x='130',y='150')
dg=Radiobutton(p,text='ยูโรทู',variable=abc,value=4,state="disabled")
dg.pack()
dg.place(x='223',y='150')
gd=Radiobutton(p,text='สีขาวน้ำเงิน',variable=abc,value=5,state="disabled")
gd.pack()
gd.place(x='275',y='150')
ry=Radiobutton(p,text='ครีมแดง',variable=abc,value=6,state="disabled")
ry.pack()
ry.place(x='20',y='180')
ui=Radiobutton(p,text='ครีมน้ำเงิน',variable=abc,value=7,state="disabled")
ui.pack()
ui.place(x='90',y='180')


def Try(event):
    if tt.get() == 33:
        jj=ttk.Combobox(p,value=f11,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f11,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="disabled")
        god.config(state="disabled")
        doo.config(state="disabled")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="disabled")
        ui.config(state="disabled")
    elif tt.get() == 203:
        jj=ttk.Combobox(p,value=f12,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f12,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="normal")
        god.config(state="normal")
        doo.config(state="normal")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="disabled")
        ui.config(state="disabled")
    elif tt.get() == 97:
        jj=ttk.Combobox(p,value=f13,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f13,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="normal")
        god.config(state="disabled")
        doo.config(state="normal")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="disabled")
        ui.config(state="disabled")
    elif tt.get() == 32:
        jj=ttk.Combobox(p,value=f14,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f14,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="disabled")
        god.config(state="disabled")
        doo.config(state="normal")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="normal")
        ui.config(state="normal")
    elif tt.get() == 543:
        jj=ttk.Combobox(p,value=f15,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f15,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="disabled")
        god.config(state="disabled")
        doo.config(state="disabled")
        dg.config(state="normal")
        gd.config(state="normal")
        ry.config(state="disabled")
        ui.config(state="disabled")
    elif tt.get() == 117:
        jj=ttk.Combobox(p,value=f16,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f16,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="disabled")
        god.config(state="disabled")
        doo.config(state="disabled")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="disabled")
        ui.config(state="disabled")      
    elif tt.get() == 64:
        jj=ttk.Combobox(p,value=f17,textvariable=play,state="readonly")
        jj.pack()
        jj.place(x="150",y="30")
        jj2=ttk.Combobox(p,value=f17,textvariable=end,state="readonly")
        jj2.pack()
        jj2.place(x="170",y=("75"))
        dog.config(state="disabled")
        god.config(state="disabled")
        doo.config(state="disabled")
        dg.config(state="disabled")
        gd.config(state="disabled")
        ry.config(state="normal")
        ui.config(state="normal")
        
def cal():    
    try:
        for op in range(103):
            for po in range(103):
                if play.get() == f11[op] and end.get() == f11[po]:
                    pay='10 บาท'
                
        for go in range(70):
            for og in range(70):
                if play.get() == f12[go] and end.get() == f12[og]:
                    if abc.get() == 1:
                        pay='สีชมพู 10 บาท'
                    elif abc.get() == 2:
                        pay='สีส้ม 12 บาท'
                    elif abc.get() == 3:
                        pay='รถแอร์สีเหลือง 14 บาท'
            if play.get() == f12[go] and end.get() == f12[go]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        for co in range(64):
            for oc in range(64):
                if play.get() == f13[co] and end.get() == f13[oc]:
                    if abc.get() == 1:
                        pay='สีชมพู 10 บาท'
                    elif abc.get() == 3:
                        pay='รถแอร์สีเหลือง 14 บาท'
            if play.get() == f13[co] and end.get() == f13[co]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        for eo in range(73):
            for oe in range(73):
                if play.get() == f14[eo] and end.get() == f14[oe]:
                    if abc.get() == 6:
                      pay='ครีมแดง'
                    elif abc.get() == 7:
                        pay='ครีมน้ำเงิน 15 บาท'
                    elif abc.get() == 3:
                        pay='รถแอร์สีเหลือง 14 บาท'
            if play.get() == f14[eo] and end.get() == f14[eo]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")         
                    
        for ao in range(46):
            for oa in range(46):
                if play.get() == f15[ao] and end.get() == f15[oa]:
                   if abc.get() == 4:
                      pay='ยูโรทู 13 บาท'
                   elif abc.get() == 5:
                      pay='สีขาวน้ำเงิน 10 บาท'
            if play.get() == f15[ao] and end.get() == f15[ao]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        for bo in range(55):
            for ob in range(55):
                if play.get() == f16[bo] and end.get() == f16[ob]:
                    pay="8 บาท"
            if play.get() == f16[bo] and end.get() == f16[bo]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        for jkl in range(41):
            for lk in range(41):
                if play.get() == f17[jkl] and end.get() == f17[lk]:
                    if abc.get() == 6:
                        pay="ครีมแดง 8 บาท"
                    elif abc.get() == 7:
                        pay="ครีมน้ำเงิน 15 บาท"
            if play.get() == f17[jkl] and end.get() == f17[jkl]:
                messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        fb.config(text=pay)
        with open("pjtk.txt","a",encoding="utf-8")as aaa:
            aaa.write("สถานีต้นทาง "+play.get())
            aaa.write(" สถานีปลายทาง "+end.get())
            aaa.write(pay+"\n")
        for df in range(103):
            if play.get() == f11[df] and end.get() == f11[df]:
                    messagebox.showerror("warning","กรุณาเลือกสถานีใหม่")
        

    except Exception:
        messagebox.showwarning("warning","กรุณากรอกข้อมูลให้ครบถ้วน")
def Kpo():
    zz=Tk()
    zz.title("History Page")
    tyu=Text(zz,width=70,height=25)
    dee=open("pjtk.txt","r",encoding="utf-8")
    ufo=dee.read()
    tyu.insert(END,ufo)
    dee.close()
    tyu.pack()

sxcdfgh=Button(p,text="View History",command=Kpo)
sxcdfgh.pack()
sxcdfgh.place(x="150",y="270")
    
tt=IntVar()
po=[33,203,97,32,543,117,64]
#aa=ttk.Combobox(p,Value="").pack
ppo=ttk.Combobox(p,value=po,width=6,textvariable=tt)
ppo.pack()
ppo.place(x="300",y="30")
ppo.bind("<<ComboboxSelected>>",Try)

a = Label(p,text="รวมราคาทั้งสิ้น(ตามระยะทาง) = ",font="20",background="light yellow")
a.pack()
a.place(x="20",y="110")

fb=Label(p,text="0 บาท",font="20")
fb.pack()
fb.place(x="290",y="110")


g = Button(p,text='OK',bg='light pink',font='10',width='10',command=cal)
g.pack()
g.place(x="150",y="230")


p.mainloop()



