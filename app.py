import streamlit as st
# إعداد الصفحة
st.set_page_config(
   page_title="حكاية وعي وأمان",
   page_icon="🛡️",
   layout="centered"
)
# تنسيق الصفحة باللغة العربية
st.markdown("""
<style>
.stApp {
   direction: rtl;
   text-align: right;
   background: linear-gradient(135deg, #f5f1fa, #edf5fa);
}
h1, h2, h3, p, label, div {
   text-align: right;
}
.main-title {
   background: linear-gradient(90deg, #8e44ad, #d65d85);
   color: white;
   padding: 25px;
   border-radius: 18px;
   text-align: center !important;
   font-size: 32px;
   font-weight: bold;
}
.story-card {
   background-color: white;
   padding: 25px;
   border-radius: 18px;
   border-right: 6px solid #a66bbe;
   line-height: 2.2;
   font-size: 19px;
   color: #303040;
   margin-top: 15px;
}
.message {
   background-color: #fceaf1;
   padding: 18px;
   border-radius: 14px;
   color: #873c61;
   font-size: 19px;
   line-height: 2;
}
.stButton button {
   width: 100%;
   border-radius: 12px;
   font-size: 18px;
   font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
# تهيئة المتغيرات
if "scene" not in st.session_state:
   st.session_state.scene = 0
if "choice" not in st.session_state:
   st.session_state.choice = None
if "quiz_done" not in st.session_state:
   st.session_state.quiz_done = False
# العنوان
st.markdown("""
<div class="main-title">
   🛡️ حكاية وعي وأمان
<div style="font-size:19px; margin-top:10px;">
   كن داعماً... لا متنمراً إلكترونياً
</div>
</div>
""", unsafe_allow_html=True)
st.write("")
st.caption("قصة رقمية تفاعلية | إعداد: قسم الحاسوب")
scenes = [
   {
       "title": "المشهد الأول: رسالة غير متوقعة",
       "text": """
       في صباح يوم دراسي، استيقظت نور على أصوات
       الإشعارات المتتابعة في هاتفها.
       فتحت مجموعة الصف، لتجد صورة لها انتشرت
       دون إذنها، مصحوبة بتعليقات ساخرة وضحكات
       من بعض زميلاتها.
       شعرت نور بالحزن والارتباك، وأغلقت هاتفها
       وهي تتساءل: لماذا يحدث هذا لي؟
       """,
       "message": "وراء كل شاشة إنسان له مشاعر وكرامة."
   },
   {
       "title": "المشهد الثاني: أثر لا يُرى",
       "text": """
       في المدرسة، لاحظت المعلمة أن نور أصبحت
       قليلة الكلام، وتفضّل الجلوس بمفردها.
       لم تكن الإساءة مجرد كلمات على شاشة،
       بل تركت أثراً في ثقتها بنفسها وشعورها بالأمان.
       وفي تلك اللحظة، شاهدت مريم ما حدث في المجموعة،
       وأدركت أن الصمت قد يسمح باستمرار الإساءة.
       """,
       "message": "الكلمة التي تكتبها قد تنتهي بضغطة زر، لكن أثرها قد يبقى طويلاً."
   },
   {
       "title": "المشهد الثالث: لحظة الاختيار",
       "text": """
       فتحت مريم هاتفها، ورأت الرسائل المسيئة تنتشر
       بين الطالبات.
       توقفت قليلاً، وفكرت: ما التصرف الصحيح
       الذي يمكن أن يوقف هذا الأذى ويحمي نور؟
       """
   },
   {
       "title": "المشهد الرابع: لكل قرار أثر",
       "text": """
       اتخذت مريم موقفها، وأدركت أن المسؤولية
       الرقمية تبدأ من تصرفاتنا اليومية.
       لم تعد تنظر إلى ما يحدث باعتباره مجرد
       مزاح أو رسائل عابرة، بل مسؤولية تستدعي
       الوعي والشجاعة.
       """
   },
   {
       "title": "المشهد الخامس: بداية الأمان",
       "text": """
       أبلغت مريم المعلمة المسؤولة، وساعدت نور
       على توثيق الإساءة والإبلاغ عنها.
       تحدثت المعلمة مع الطالبات، ووضحت لهن
       أن احترام الآخرين واجب في العالم الرقمي
       كما هو في الواقع.
       عادت نور إلى صفها وهي تشعر أن هناك
       من يقف بجانبها، وأنها ليست وحدها.
       أما مريم، فقد أدركت أن موقفاً إيجابياً
       واحداً قد يصنع فرقاً كبيراً في حياة إنسان.
       """,
       "message": "كن جزءاً من الحل، ولا تكن جزءاً من الإساءة."
   }
]
# عرض مؤشر التقدم
st.progress((st.session_state.scene + 1) / len(scenes))
st.caption(
   f"المشهد {st.session_state.scene + 1} من {len(scenes)}"
)
# عرض أحداث القصة
scene = scenes[st.session_state.scene]
st.subheader(scene["title"])
st.markdown(
   f'<div class="story-card">{scene["text"].replace(chr(10), "<br>")}</div>',
   unsafe_allow_html=True
)
# الرسالة التوعوية
if "message" in scene:
   st.markdown(
       f'<div class="message">💡 {scene["message"]}</div>',
       unsafe_allow_html=True
   )
# المشهد التفاعلي
if st.session_state.scene == 2:
   st.write("")
   st.markdown("### ماذا ستفعلين لو كنتِ مكان مريم؟")
   choice = st.radio(
       "اختاري التصرف الذي ترينه صحيحاً:",
       [
           "إعادة إرسال الصورة ومشاركة التعليقات.",
           "تجاهل الموقف وعدم التدخل.",
           "دعم نور، وعدم نشر الصورة، والإبلاغ عن الإساءة."
       ],
       key="decision"
   )
   if st.button("اتخاذ القرار"):
       st.session_state.choice = choice
       st.session_state.scene = 3
       st.rerun()
# نتيجة الاختيار
elif st.session_state.scene == 3:
   if st.session_state.choice == "إعادة إرسال الصورة ومشاركة التعليقات.":
       st.error("""
       هذا التصرف يزيد انتشار الإساءة، وقد يضاعف
       الأذى النفسي الذي تتعرض له نور.
       تذكري: إعادة نشر المحتوى المسيء تساهم
       في استمرار التنمر الإلكتروني.
       """)
   elif st.session_state.choice == "تجاهل الموقف وعدم التدخل.":
       st.warning("""
       الصمت لا يوقف الإساءة دائماً، وقد يشعر
       الشخص المتضرر بأنه وحيد.
       يمكنك المساعدة دون تعريض نفسك للخطر،
       من خلال الإبلاغ وطلب مساعدة شخص موثوق.
       """)
   else:
       st.success("""
       أحسنتِ! هذا هو التصرف المسؤول.
       دعم المتضرر، وعدم نشر المحتوى المسيء،
       وتوثيق الإساءة والإبلاغ عنها خطوات
       تساعد على حماية الآخرين.
       """)
st.info("لننتقل إلى نهاية الحكاية ونتعرف إلى أثر الوعي الرقمي.")
# أزرار التنقل
if st.session_state.scene < len(scenes) - 1:
   if st.session_state.scene != 2:
       if st.button("متابعة القصة ←"):
           st.session_state.scene += 1
           st.rerun()
else:
   st.divider()
   st.markdown("""
<div class="main-title">
       🌷 كن داعماً... لا متنمراً
<div style="font-size:20px; margin-top:12px;">
       كن صوتاً لمن لا يستطيع الكلام،
       وساهم في نشر الأمان الرقمي.
</div>
</div>
   """, unsafe_allow_html=True)
   st.write("")
   st.subheader("🧠 اختبري وعيك الرقمي")
   answer = st.radio(
       "ما التصرف الصحيح عند مشاهدة محتوى مسيء لشخص آخر؟",
       [
           "إعادة نشره لتحذير الآخرين.",
           "التعليق عليه بالسخرية.",
           "عدم نشره، وتوثيقه، والإبلاغ عنه."
       ],
       key="quiz_answer"
   )
   if st.button("تحقق من إجابتي"):
       st.session_state.quiz_done = True
       if answer == "عدم نشره، وتوثيقه، والإبلاغ عنه.":
           st.success("إجابة صحيحة! أنتِ سفيرة للوعي والأمان الرقمي. 🌟")
       else:
           st.error("حاولي مرة أخرى. تذكري أن نشر المحتوى المسيء يزيد انتشاره.")
   if st.button("إعادة القصة من البداية"):
       st.session_state.scene = 0
       st.session_state.choice = None
       st.session_state.quiz_done = False
       st.rerun()
st.write("")
st.caption("إنتاج رقمي توعوي | لا للتنمر الإلكتروني")