
import streamlit as st

# ==========================================
# إعداد الصفحة
# ==========================================
st.set_page_config(
    page_title="حكاية وعي وأمان",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# تنسيق الموقع والخطوط
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap');

:root {
    --purple: #7451A6;
    --pink: #D978A4;
    --light: #F8F4FC;
    --dark: #302742;
    --muted: #756B80;
}

html, body, [class*="css"] {
    font-family: 'Cairo', Tahoma, sans-serif !important;
}

.stApp {
    background: linear-gradient(145deg, #F8F4FC, #FDF4F8);
    direction: rtl;
}

[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 950px;
    padding: 2rem 2rem 3rem;
}

p, label, li, .stMarkdown {
    font-family: 'Cairo', Tahoma, sans-serif !important;
    color: var(--dark);
    font-size: 19px !important;
    line-height: 2 !important;
    text-align: right;
}

h1, h2, h3 {
    font-family: 'Cairo', Tahoma, sans-serif !important;
    color: var(--dark) !important;
    font-weight: 800 !important;
    text-align: right;
}

.hero {
    background: linear-gradient(120deg, #7451A6, #C66C9B);
    color: white;
    padding: 42px 25px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 9px 25px rgba(116,81,166,0.18);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 39px;
    font-weight: 900;
    color: white;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 22px;
    color: white;
    font-weight: 600;
}

.section-card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #EEE5F5;
    box-shadow: 0 5px 18px rgba(80,50,100,0.06);
    margin: 18px 0;
    font-size: 21px;
    line-height: 2.2;
    color: #302742;
}

.scene-number {
    color: #A36BB8;
    font-size: 16px;
    font-weight: 800;
}

.scene-title {
    font-size: 27px;
    font-weight: 900;
    color: #7451A6;
    margin: 8px 0 18px;
}

.story-text {
    font-size: 21px;
    line-height: 2.3;
    color: #40364C;
    white-space: pre-line;
}

.tip {
    background: #F8EDF5;
    border-right: 6px solid #D978A4;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    font-size: 19px;
    color: #78496D;
    line-height: 2;
}

.final-card {
    background: linear-gradient(135deg, #7451A6, #D978A4);
    color: white;
    padding: 35px 25px;
    border-radius: 24px;
    text-align: center;
    margin-top: 20px;
}

.final-card h2, .final-card p {
    color: white !important;
    text-align: center !important;
}

div.stButton > button {
    width: 100%;
    min-height: 55px;
    border-radius: 15px;
    background: #7451A6;
    color: white;
    font-family: 'Cairo', Tahoma, sans-serif;
    font-size: 19px;
    font-weight: 800;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: #D978A4;
    color: white;
    border: none;
}

div[data-testid="stRadio"] label {
    font-size: 18px !important;
    line-height: 2 !important;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #7451A6, #D978A4);
}

.footer {
    text-align: center;
    color: #95869F;
    font-size: 15px;
    padding-top: 30px;
}

@media(max-width: 600px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    .hero-title {
        font-size: 29px;
    }

    .hero-subtitle {
        font-size: 18px;
    }

    .section-card {
        padding: 20px;
    }

    .scene-title {
        font-size: 23px;
    }

    .story-text {
        font-size: 19px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# إدارة مراحل القصة
# ==========================================

if "stage" not in st.session_state:
    st.session_state.stage = 0

if "decision" not in st.session_state:
    st.session_state.decision = None

if "decision_error" not in st.session_state:
    st.session_state.decision_error = False

if "quiz_checked" not in st.session_state:
    st.session_state.quiz_checked = False

if "quiz_correct" not in st.session_state:
    st.session_state.quiz_correct = False


def next_stage():
    st.session_state.stage += 1


def confirm_decision():
    choice = st.session_state.get("decision_radio")

    if choice is None:
        st.session_state.decision_error = True
    else:
        st.session_state.decision = choice
        st.session_state.decision_error = False
        st.session_state.stage = 4


def check_quiz():
    answer = st.session_state.get("final_quiz")

    if answer is not None:
        st.session_state.quiz_checked = True
        st.session_state.quiz_correct = (
            answer == "عدم نشره، وتوثيقه، والإبلاغ عنه."
        )


def restart():
    st.session_state.stage = 0
    st.session_state.decision = None
    st.session_state.decision_error = False
    st.session_state.quiz_checked = False
    st.session_state.quiz_correct = False

    st.session_state.pop("decision_radio", None)
    st.session_state.pop("final_quiz", None)


# ==========================================
# رأس الموقع
# ==========================================

st.markdown("""
<div class="hero">
    <div style="font-size:52px;">🛡️</div>
    <div class="hero-title">حكاية وعي وأمان</div>
    <div class="hero-subtitle">
        كن داعماً... لا متنمراً إلكترونياً
    </div>
    <div style="font-size:16px; margin-top:15px;">
        رحلة تفاعلية نحو عالم رقمي أكثر أماناً
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# بيانات القصة
# ==========================================

story = {
    1: {
        "number": "المشهد الأول | البداية",
        "title": "رسالة غيّرت يومها",
        "text": """
في صباح يوم دراسي، استيقظت نور على أصوات
الإشعارات المتتابعة في هاتفها.
فتحت مجموعة الصف، لتجد صورة لها انتشرت
دون إذنها، مصحوبة بتعليقات ساخرة وضحكات.
شعرت نور بالحزن والارتباك، وأغلقت هاتفها
وهي تتساءل: لماذا يحدث هذا لي؟
""",
        "tip": "وراء كل شاشة إنسان له مشاعر وكرامة. فاحرصي على احترام الآخرين في كل ما تنشرينه."
    },

    2: {
        "number": "المشهد الثاني | الأثر",
        "title": "أثر لا يُرى",
        "text": """
في المدرسة، لاحظت المعلمة أن نور أصبحت
قليلة الكلام، وتفضّل الجلوس بمفردها.
لم تكن الإساءة مجرد كلمات على شاشة،
بل تركت أثراً في ثقتها بنفسها وشعورها بالأمان.
وفي تلك اللحظة، شاهدت مريم ما حدث في المجموعة،
وأدركت أن الصمت قد يسمح باستمرار الإساءة.
""",
        "tip": "قد تختفي الرسالة من الشاشة، لكن أثرها النفسي قد يستمر. لا تستهيني بقوة الكلمة."
    }
}


# ==========================================
# المرحلة صفر: شاشة البداية
# ==========================================

if st.session_state.stage == 0:

    st.markdown("""
    <div class="section-card" style="text-align:center;">
        <div style="font-size:55px;">🌷</div>
        <div style="font-size:26px;font-weight:900;color:#7451A6;">
            لكل كلمة أثر... ولكل موقف قرار
        </div>
        <p style="text-align:center !important;">
            في عالم تتسارع فيه الرسائل والمنشورات،
            قد تتحول ضغطة زر إلى مصدر للأذى،
            وقد تتحول كلمة طيبة إلى بداية للأمان.
        </p>
        <p style="text-align:center !important;">
            تعرّفي إلى حكاية نور ومريم،
            واكتشفي كيف يمكن لموقف شجاع
            أن يغيّر حياة إنسان.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("💡 أثناء القصة ستواجهين مواقف تتطلب منك اتخاذ قرارات. اختاري بحكمة!")

    st.button(
        "ابدئي الحكاية 🌸",
        on_click=next_stage
    )


# ==========================================
# المرحلة الأولى والثانية: المشاهد
# ==========================================

elif st.session_state.stage in [1, 2]:

    st.progress(st.session_state.stage / 5)

    scene = story[st.session_state.stage]

    st.markdown(f"""
    <div class="section-card">
        <div class="scene-number">{scene['number']}</div>
        <div class="scene-title">{scene['title']}</div>
        <div class="story-text">{scene['text']}</div>
        <div class="tip">💡 {scene['tip']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.button(
        "متابعة القصة ←",
        on_click=next_stage
    )


# ==========================================
# المرحلة الثالثة: لحظة اتخاذ القرار
# ==========================================

elif st.session_state.stage == 3:

    st.progress(3 / 5)

    st.markdown("""
    <div class="section-card">
        <div class="scene-number">المشهد الثالث | لحظة الاختيار</div>
        <div class="scene-title">ماذا ستفعلين لو كنتِ مكان مريم؟</div>
        <div class="story-text">
            فتحت مريم هاتفها، ورأت الرسائل المسيئة تنتشر
            بين الطالبات.

            توقفت قليلاً، وفكرت:

            هل أشارك في نشر الإساءة؟
            هل أتجاهل ما يحدث؟
            أم أتخذ موقفاً يحمي نور ويوقف انتشار التنمر؟
        
    </div>
    """, unsafe_allow_html=True)

    st.radio(
        "اختاري قرارك:",
        [
            "إعادة إرسال الصورة ومشاركة التعليقات.",
            "تجاهل الموقف وعدم التدخل.",
            "دعم نور، وعدم نشر الصورة، والإبلاغ عن الإساءة."
        ],
        index=None,
        key="decision_radio"
    )

    if st.session_state.decision_error:
        st.warning("يرجى اختيار أحد القرارات أولاً.")

    st.button(
        "تأكيد القرار",
        on_click=confirm_decision
    )


# ==========================================
# المرحلة الرابعة: نتيجة القرار
# ==========================================

elif st.session_state.stage == 4:

    st.progress(4 / 5)

    decision = st.session_state.decision

    if decision == "إعادة إرسال الصورة ومشاركة التعليقات.":

        title = "قرار يزيد الألم"
        result = """
إعادة إرسال الصورة تساهم في انتشار الإساءة
وتضاعف الأذى الذي تتعرض له نور.

قد تظنين أن الأمر مجرد مزاح،
لكن المشاركة في نشر المحتوى المسيء
تجعلك جزءاً من المشكلة.
"""
        tip = "لا تعيدي نشر أي محتوى ينتهك خصوصية الآخرين أو يسخر منهم."
        icon = "⚠️"

    elif decision == "تجاهل الموقف وعدم التدخل.":

        title = "الصمت لا يكفي دائماً"
        result = """
قد لا تكونين مشاركة في الإساءة،
لكن نور قد تشعر بأنها وحيدة.

يمكنك تقديم المساعدة بطريقة آمنة،
من خلال طلب دعم المعلمة أو شخص موثوق
والإبلاغ عن السلوك المسيء.
"""
        tip = "لا تعرضي نفسك للخطر، ولكن لا تتركي المتضرر دون مساندة."
        icon = "💜"

    else:

        title = "قرار يصنع الفرق"
        result = """
أحسنتِ! لقد اخترتِ التصرف المسؤول.

دعم نور، وعدم نشر الصورة،
وتوثيق الإساءة والإبلاغ عنها
خطوات تساعد على إيقاف التنمر.

لقد أصبحتِ جزءاً من الحل،
وساهمتِ في نشر الأمان الرقمي.
"""
        tip = "كلمة دعم واحدة قد تمنح إنساناً القوة لمواجهة موقف صعب."
        icon = "🌟"

    st.markdown(f"""
    <div class="section-card">
        <div style="text-align:center;font-size:55px;">{icon}</div>
        <div class="scene-title" style="text-align:center;">
            {title}
        </div>
        <div class="story-text" style="text-align:center;">
            {result}
        </div>
        💡 {tip}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### وماذا حدث بعد ذلك؟")

    if decision == "دعم نور، وعدم نشر الصورة، والإبلاغ عن الإساءة.":

        st.success("""
        ساعدت مريم نور على توثيق الإساءة والإبلاغ عنها،
        وطلبتا مساعدة المعلمة.

        عادت نور إلى صفها وهي تشعر أن هناك
        من يقف بجانبها.
        """)

    else:

        st.info("""
        لاحظت مريم أن الإساءة لم تتوقف،
        فأدركت أن عليها إعادة التفكير في موقفها.

        قررت في النهاية مساندة نور وطلب المساعدة
        من المعلمة المسؤولة.
        """)

    st.markdown("""
    <div class="tip">
        تذكري: يمكنك دائماً تصحيح موقفك واختيار
        التصرف المسؤول.
    </div>
    """, unsafe_allow_html=True)

    st.button(
        "اكتشفي نهاية الحكاية ←",
        on_click=next_stage
    )


# ==========================================
# المرحلة الخامسة: الخاتمة والاختبار
# ==========================================

elif st.session_state.stage == 5:

    st.progress(1.0)

    st.markdown("""
    <div class="final-card">
        <div style="font-size:55px;">🌷</div>
        <h2>نهاية الحكاية... وبداية مسؤوليتك</h2>
        <p>
            قد لا تستطيعين منع كل رسالة مؤذية،
            لكنك تستطيعين أن تكوني سبباً في إيقاف انتشارها.
        </p>
        <h2>كن داعماً... لا متنمراً إلكترونياً</h2>
        <p>كن صوتاً لمن لا يستطيع الكلام.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🧠 اختبري وعيك الرقمي")

    st.markdown("""
    <div class="section-card">
        ماذا تفعلين عند مشاهدة محتوى مسيء
        لشخص آخر في إحدى المجموعات؟
    </div>
    """, unsafe_allow_html=True)

    st.radio(
        "اختاري الإجابة الصحيحة:",
        [
            "إعادة نشره لتحذير الآخرين.",
            "التعليق عليه بالسخرية.",
            "عدم نشره، وتوثيقه، والإبلاغ عنه."
        ],
        index=None,
        key="final_quiz"
    )

    st.button(
        "تحققي من إجابتك",
        on_click=check_quiz
    )

    if st.session_state.quiz_checked:

        if st.session_state.quiz_correct:

            st.success(
                "إجابة صحيحة! أنتِ سفيرة للوعي والأمان الرقمي 🌟"
            )
            st.balloons()

            st.markdown("""
            <div class="tip">
                🌟 تذكري دائماً:

                ١. احترمي خصوصية الآخرين.

                ٢. لا تنشري الرسائل أو الصور المسيئة.

                ٣. أبلغي عن التنمر واطلبي المساعدة.

                ٤. كوني داعمة للمتضررين.
            </div>
            """, unsafe_allow_html=True)

        else:

            st.error(
                "ليست الإجابة الصحيحة. فكري في الطريقة التي تحمي المتضرر وتوقف انتشار الإساءة."
            )

    st.button(
        "🔄 إعادة الحكاية من البداية",
        on_click=restart
    )


# ==========================================
# تذييل الموقع
# ==========================================

st.markdown("""
<div class="footer">
    🛡️ حكاية وعي وأمان
    <br>
    إنتاج رقمي توعوي | لا للتنمر الإلكتروني
    <br>
    معاً نصنع بيئة رقمية آمنة ومحترمة
</div>
""", unsafe_allow_html=True)
