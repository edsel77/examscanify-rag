"""
ExamScanify Knowledge Base
~80+ curated chunks across 4 categories:
  - landing      : public landing page content
  - mobile-app   : Android app internals
  - backend      : API & cloud infrastructure
  - web-console  : examscanify web console
"""

KNOWLEDGE_CHUNKS = [
    # ─────────────────────────────────────────────
    # LANDING PAGE
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify is the #1 ZipGrade alternative for DepEd teachers in the Philippines. "
            "It provides fast, accurate MDAT exam scanning and automated grading with zero monthly scan limits. "
            "Teachers can grade unlimited exams for free or unlock the Premium Pass for a low annual fee of ₱299/year. "
            "It is designed specifically for the Philippine educational system and DepEd curriculums. "
            "The app is available on Android via Google Play (package: com.driftapps.scanify). "
            "The developer is Drift Apps. The official website is https://examscanify.com."
        ),
        "metadata": {"category": "landing", "title": "ExamScanify Overview"},
    },
    {
        "content": (
            "ExamScanify's hero tagline is 'Smart Mobile Exam Scanning.' "
            "It is powered by OpenCV technology for computer vision-based bubble sheet detection. "
            "Key highlights shown on the landing page: Unlimited Scanning, AI Exam Generation, Secured Cloud Storage. "
            "Two primary CTAs are available: Download App (links to Google Play) and Web Console (links to console.examscanify.com). "
            "The app scans and grades unlimited exams directly from a mobile phone. "
            "It auto-detects exam and student data instantly from printed sheet codes. "
            "Results can be exported to Excel in one tap."
        ),
        "metadata": {"category": "landing", "title": "Hero Section & Value Proposition"},
    },
    {
        "content": (
            "ExamScanify key performance stats shown on the landing page: "
            "99.9% accuracy rate for bubble detection; "
            "less than 1 second scan time per sheet; "
            "real-time cloud processing for instant results; "
            "Premium Pass priced at ₱299 per year (~$5 USD at 0.017 exchange rate)."
        ),
        "metadata": {"category": "landing", "title": "Key Stats & Performance Metrics"},
    },
    {
        "content": (
            "ExamScanify Pricing — Free Plan (named 'Free Forever', costs ₱0): "
            "No monthly scanning limits; "
            "AI MDAT Exam Generation included; "
            "Unified Smart Auto-Detection included; "
            "Item Analysis & Data Exports included; "
            "Web console access included; "
            "Contains ads (free users see rewarded ads to unlock extra scan sessions). "
            "The free plan is described as 'Essential tools for every teacher.'"
        ),
        "metadata": {"category": "landing", "title": "Pricing: Free Plan"},
    },
    {
        "content": (
            "ExamScanify Pricing — Premium Pass (annual plan, ₱299/year, ~$5 USD/year): "
            "No advertisements — completely ad-free experience; "
            "Realtime web console sync — cloud data always up to date; "
            "Supports development of ExamScanify; "
            "Badge label: '⚡ Power Up'; "
            "Billed annually, cancel anytime before renewal. "
            "Described as 'Full premium access for a year' and 'Ultimate value for teachers.' "
            "Purchase is a one-time annual payment, not auto-renewing subscription."
        ),
        "metadata": {"category": "landing", "title": "Pricing: Premium Pass"},
    },
    {
        "content": (
            "ExamScanify Feature: Unified Smart Detection. "
            "One scanner handles all exam types simultaneously. "
            "The app automatically identifies which exam is being graded and which student it belongs to "
            "from dedicated codes embedded in each printed answer sheet. "
            "No manual sorting, folder switching, or settings changes required. "
            "Teachers can scan a mixed stack of answer sheets from different exams in a single pass."
        ),
        "metadata": {"category": "landing", "title": "Feature: Unified Smart Detection"},
    },
    {
        "content": (
            "ExamScanify Feature: Secured Cloud Storage. "
            "All student names, codes, and exam scores are securely synced to an encrypted cloud infrastructure. "
            "Data is accessible from any device or from the web console at console.examscanify.com. "
            "Industry-standard encryption protects all cloud-stored data. "
            "Free users get cloud sync access; Premium users get realtime sync."
        ),
        "metadata": {"category": "landing", "title": "Feature: Secured Cloud Storage"},
    },
    {
        "content": (
            "ExamScanify Feature: Item Analysis. "
            "Provides detailed per-question analytics showing the distribution of student answers. "
            "Identifies which questions students found most challenging. "
            "Includes distractor analysis: shows which wrong answers students chose most frequently, "
            "helping teachers identify specific misconceptions in the class."
        ),
        "metadata": {"category": "landing", "title": "Feature: Item Analysis & Analytics"},
    },
    {
        "content": (
            "ExamScanify Feature: Class Management. "
            "Teachers can organize students by class section. "
            "Track student progress over time across multiple exams. "
            "Manage multiple class sections effortlessly. "
            "Each class has a section name and grade level. "
            "Students are enrolled per class with unique student codes used for auto-detection during scanning."
        ),
        "metadata": {"category": "landing", "title": "Feature: Class Management"},
    },
    {
        "content": (
            "ExamScanify Feature: Excel Export. "
            "Generate professional Excel reports from any exam result. "
            "Reports include student scores, percentages, and analytics. "
            "Can be shared via email or saved to cloud storage. "
            "To export: open any exam and tap the Share icon; ExamScanify generates the Excel file automatically."
        ),
        "metadata": {"category": "landing", "title": "Feature: Excel Export"},
    },
    {
        "content": (
            "ExamScanify Feature: Real-time Cloud Processing. "
            "Advanced cloud infrastructure enables lightning-fast scanning and real-time data processing. "
            "Scan results are processed and saved instantly after each sheet is captured. "
            "Cloud sync keeps data consistent across the mobile app and web console."
        ),
        "metadata": {"category": "landing", "title": "Feature: Real-time Cloud Processing"},
    },
    {
        "content": (
            "ExamScanify AI Exam Generation — Featured Innovation. "
            "The AI Exam Generator automatically creates high-quality MDAT exams tailored to the teacher's subject and topic. "
            "Features: Instant MDAT question generation; Automatic answer key population; Perfect for DepEd curriculums. "
            "Stop spending hours writing questions — AI handles question creation, choice generation, and answer key in seconds. "
            "Available as the 'Creator' tab in the mobile app. "
            "Uses Gemini AI on the backend."
        ),
        "metadata": {"category": "landing", "title": "Feature: AI-Powered Exam Generation"},
    },
    {
        "content": (
            "ExamScanify Analytics section highlights two capabilities: "
            "1. Performance Benchmarking — compare exam results across multiple classes and exam versions effortlessly. "
            "2. Distractor Analysis — see which wrong answers students are choosing to identify specific misconceptions. "
            "Analytics screenshots show: Performance Insights screen, Item Analysis screen, and Class Comparison screen in the mobile app."
        ),
        "metadata": {"category": "landing", "title": "Analytics: Performance & Distractor Analysis"},
    },
    {
        "content": (
            "ExamScanify Printable Outputs — Answer Sheets. "
            "The app generates personalized answer sheets for every student in a class. "
            "Each sheet is pre-printed with the student's name, class code, and unique student ID. "
            "Layout: 6 students per page to save paper; includes ExamScanify watermark for authenticity. "
            "The sheet's embedded code is automatically read by the scanner during grading — no manual selection needed. "
            "Teachers print these sheets and distribute them before the exam."
        ),
        "metadata": {"category": "landing", "title": "Printable Output: Answer Sheets"},
    },
    {
        "content": (
            "ExamScanify Printable Outputs — AI-Generated Question Papers. "
            "The AI Exam Generator produces complete, DepEd-aligned MDAT question papers ready for printing. "
            "Each document includes: full scenario-based MDAT questions; point-based Key to Correction table with values per answer choice. "
            "Exported as .docx format, editable in Microsoft Word. "
            "Tailored to DepEd subject competencies. "
            "No manual formatting required — the AI handles the full document layout."
        ),
        "metadata": {"category": "landing", "title": "Printable Output: AI Question Papers (.docx)"},
    },
    {
        "content": (
            "How ExamScanify Works — Step 1: Create Your Exam. "
            "Teachers create exams manually using Classic mode (right/wrong scoring) or MDAT mode (rubric-based point weights per answer choice). "
            "Alternatively, use the AI Exam Generator to instantly create MDAT questions tailored for DepEd subjects. "
            "Exams support 1 to 60 items. Item counts available in AI generator: 10, 20, 30, 40, 50."
        ),
        "metadata": {"category": "landing", "title": "How It Works: Step 1 — Create Exam"},
    },
    {
        "content": (
            "How ExamScanify Works — Step 2: One Scanner Fits All. "
            "No need to switch folders or settings between different exams. "
            "Use a single scanner for all exams simultaneously. "
            "The app automatically detects the student's identity and the exam type from codes printed on the answer sheet. "
            "Scan a mixed stack of sheets from different classes and exams in one continuous session."
        ),
        "metadata": {"category": "landing", "title": "How It Works: Step 2 — Unified Scanner"},
    },
    {
        "content": (
            "How ExamScanify Works — Step 3: Analyze & Export. "
            "After scanning, view detailed analytics and student performance trends. "
            "Export results to Excel for reporting. "
            "Access all recorded grades and analytics on desktop via console.examscanify.com. "
            "Web console provides: Classes & Students view, Exam Scores, Overall Summary, Performance by Class, Item Analysis, and Answer Sheet downloads."
        ),
        "metadata": {"category": "landing", "title": "How It Works: Step 3 — Analyze & Export"},
    },
    {
        "content": (
            "ExamScanify FAQ: How does scanning work? "
            "The app uses OpenCV technology to detect 6 black corner markers on the answer sheet. "
            "Green indicators confirm all 6 markers are found. "
            "Once aligned, the app automatically captures and processes the image. "
            "It detects shaded bubbles and calculates the score in real-time based on the exam's stored answer key."
        ),
        "metadata": {"category": "landing", "title": "FAQ: How Scanning Works"},
    },
    {
        "content": (
            "ExamScanify FAQ: How does the AI Exam Generator work? "
            "The teacher specifies a subject and topic. "
            "The AI automatically generates MDAT multiple-choice questions, answer choices, and fully populates the answer key in seconds. "
            "Outputs include a printable .docx question paper and a Key to Correction. "
            "The generator supports both MDAT (rubric-based) and Classic HOTS (single correct answer) formats."
        ),
        "metadata": {"category": "landing", "title": "FAQ: AI Exam Generator"},
    },
    {
        "content": (
            "ExamScanify FAQ: Is student data safe? "
            "Yes. All student names, codes, and scores are securely synced to an encrypted cloud infrastructure. "
            "Data is protected by industry-standard encryption and accessible from any device or the web console. "
            "Student data is stored in Supabase with row-level security."
        ),
        "metadata": {"category": "landing", "title": "FAQ: Data Safety & Security"},
    },
    {
        "content": (
            "ExamScanify FAQ: Can the app be used offline? "
            "ExamScanify handles all core scanning and grading tasks on-device — no internet needed during a scan session. "
            "Student records and analytics can be managed locally. "
            "Cloud sync and AI generation require an internet connection."
        ),
        "metadata": {"category": "landing", "title": "FAQ: Offline Use"},
    },
    {
        "content": (
            "ExamScanify FAQ: What is the difference between Classic and MDAT modes? "
            "Classic mode: Traditional right/wrong scoring — each correct answer gets exactly 1 point. "
            "MDAT (Modified Difficulty-Adjusted Test) mode: Each answer choice has a different point value. "
            "MDAT allows partial credit and more nuanced assessment of student understanding. "
            "MDAT is the standard used in DepEd assessments."
        ),
        "metadata": {"category": "landing", "title": "FAQ: Classic vs MDAT Modes"},
    },
    {
        "content": (
            "ExamScanify FAQ: How do I export results? "
            "Open any exam in the app and tap the Share icon. "
            "ExamScanify generates a professional Excel file containing student scores, percentages, and analytics. "
            "The file can be shared via email, saved to cloud storage, or transferred to a computer."
        ),
        "metadata": {"category": "landing", "title": "FAQ: Exporting Results to Excel"},
    },
    {
        "content": (
            "ExamScanify FAQ: Do I need to select the exam before scanning? "
            "No. Unlike competitors that use generic answer sheets, ExamScanify uses dedicated sheets with built-in exam and student codes. "
            "The unified scanner automatically identifies which exam is being graded and which student it belongs to. "
            "Teachers can scan a mixed stack of different exams in one go without changing any settings."
        ),
        "metadata": {"category": "landing", "title": "FAQ: No Manual Exam Selection Needed"},
    },
    {
        "content": (
            "ExamScanify FAQ: Is scanning really unlimited? "
            "Yes. All users — free and premium — can scan unlimited times. "
            "Free users unlock additional scanning sessions for free by completing a brief rewarded ad interaction when prompted. "
            "Premium Pass users (₱299/year) enjoy a completely seamless, uninterrupted scanning experience with no ads and no prompts."
        ),
        "metadata": {"category": "landing", "title": "FAQ: Unlimited Scanning"},
    },
    {
        "content": (
            "ExamScanify Web Console sections (visible at console.examscanify.com): "
            "1. Classes & Students — manage class sections and enrolled students; "
            "2. Students List — full roster with student codes; "
            "3. Exams & Results — list all exams with result summaries; "
            "4. Exam Scores — per-student score table for each exam; "
            "5. Overall Summary — aggregated performance data; "
            "6. Performance by Class — compare results across sections; "
            "7. Item Analysis — per-question answer distribution; "
            "8. Download Answer Sheets — generate and download printable sheets."
        ),
        "metadata": {"category": "landing", "title": "Web Console Feature Sections"},
    },
    {
        "content": (
            "ExamScanify supported subjects for AI Exam Generation: "
            "Filipino, English, Mathematics, Science, AP (Araling Panlipunan), EsP (Edukasyon sa Pagpapakatao), "
            "Music, Arts, Physical Education, Health, EPP, TLE, "
            "Oral Communication, Reading and Writing, General Mathematics, Statistics and Probability, "
            "Earth and Life Science, Physical Science, STEM, ABM, HUMSS, TVL. "
            "Custom subjects can also be typed in manually."
        ),
        "metadata": {"category": "landing", "title": "AI Exam Generator: Supported Subjects"},
    },
    {
        "content": (
            "ExamScanify company and contact information: "
            "Developer: Drift Apps (https://drift-apps.netlify.app/). "
            "Support email: support@examscanify.com. "
            "Admin email: driftvelocity.app@gmail.com. "
            "Website: https://examscanify.com. "
            "Web Console: https://console.examscanify.com. "
            "Google Play: https://play.google.com/store/apps/details?id=com.driftapps.scanify. "
            "Android package name: com.driftapps.scanify."
        ),
        "metadata": {"category": "landing", "title": "Company & Contact Information"},
    },

    # ─────────────────────────────────────────────
    # MOBILE APP
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify Android app has 5 main tabs: "
            "1. Scanner — real-time camera scanning using OpenCV via a Vue.js WebView; "
            "2. Classes — manage class sections and students; "
            "3. Exams — create, edit, view, and delete exams; "
            "4. Creator (AI Exam Generator) — generate AI-powered MDAT or Classic exams; "
            "5. Account — membership status, data management, support, and auth settings."
        ),
        "metadata": {"category": "mobile-app", "title": "App Tabs Overview"},
    },
    {
        "content": (
            "ExamScanify Scanner Tab architecture: "
            "The scanner runs inside a React Native WebView that loads a compiled Vue.js app from local Android assets. "
            "Two scanner modes: 'standard' (scanner-form-b route) and 'lite' (scanner route). "
            "The Vue app communicates with React Native via postMessage (WebView bridge). "
            "OpenCV runs inside the Vue WebView for real-time marker detection and bubble reading. "
            "The WebView loads from: file:///android_asset/vue-dist/index.html"
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner Tab: Architecture"},
    },
    {
        "content": (
            "ExamScanify Scanner scan flow: "
            "1. Camera streams through the Vue WebView. "
            "2. OpenCV detects 6 black corner markers on the answer sheet (MARKER_DETECTED event). "
            "3. On full detection, the WebView auto-captures the image and reads shaded bubbles. "
            "4. SCAN_COMPLETED event is sent to React Native with: studentData, examData, assessmentData, "
            "correctAnswerCount, totalItems, unshadedNumbers, studentAnswers, capturedImage. "
            "5. ScanResultModal displays the result with student name, score, percentage, and captured image."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Scan Flow"},
    },
    {
        "content": (
            "ExamScanify Scanner: Battery Saver feature. "
            "The camera automatically pauses after 30 seconds of inactivity to save battery. "
            "A countdown overlay appears during the last 10 seconds (from 20s of inactivity). "
            "Activity is reset whenever a marker is detected or the user interacts with the scanner. "
            "The scanner resumes automatically when the user returns to the Scanner tab."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Battery Saver"},
    },
    {
        "content": (
            "ExamScanify Scanner: Camera Watchdog. "
            "A watchdog timer checks for camera heartbeats every 3 seconds. "
            "If no heartbeat is received for 15 seconds (indicating a freeze), the WebView is restarted. "
            "The watchdog is suppressed during scanner mode switches to avoid false restarts. "
            "A keep-alive ping is sent to the WebView every 10 seconds to prevent camera sleep."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Watchdog & Keep-Alive"},
    },
    {
        "content": (
            "ExamScanify Scanner: Scanning Limit for free users. "
            "Free users have a daily scan count limit tracked in local storage. "
            "When the limit is reached, a UsageLimitModal appears. "
            "Free users can watch a rewarded ad (via Google AdMob) to unlock extra scan time. "
            "Premium users always have isOverLimit = false — no scanning limit applies. "
            "Limit status is re-checked every 30 seconds while the scanner is open."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Scanning Limit (Free Users)"},
    },
    {
        "content": (
            "ExamScanify Scanner: Camera controls. "
            "Supports torch/flashlight toggle when the device has a flash. "
            "Supports switching between multiple camera devices (e.g., rear cameras on multi-lens phones). "
            "When switching cameras, the WebView is fully reloaded for reliability on low-end Android devices. "
            "The preferred camera ID is stored locally and restored on next session."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Camera Controls"},
    },
    {
        "content": (
            "ExamScanify Scanner: Answer key requirement. "
            "If a scanned exam has no answer key set, the app shows a NoAnswerKeyModal instead of the result. "
            "The teacher must set the answer key in the Exams tab before scanning results are processed. "
            "Answer keys are AES-encrypted before being stored locally in SQLite."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Answer Key Requirement"},
    },
    {
        "content": (
            "ExamScanify Scanner: Brightness overlay. "
            "The scanner displays a brightness indicator updated at most once per second from the Vue WebView. "
            "This helps teachers know if the lighting conditions are sufficient for accurate scanning. "
            "Low brightness warnings guide the user to improve scan conditions."
        ),
        "metadata": {"category": "mobile-app", "title": "Scanner: Brightness Overlay"},
    },
    {
        "content": (
            "ExamScanify Exams Tab. "
            "Displays a searchable list of all created exams. "
            "Search by exam name, subject, or exam ID. "
            "Each exam card shows: exam name, subject, item count, type (Classic/MDAT), sheet type. "
            "Actions: Create Exam (FAB button), view details, edit, delete, set answer key, view student results. "
            "Bulk delete: long-press to enter selection mode; select multiple exams and delete at once. "
            "Item count must be between 1 and 60."
        ),
        "metadata": {"category": "mobile-app", "title": "Exams Tab"},
    },
    {
        "content": (
            "ExamScanify Exams Tab: Sheet types. "
            "Each exam can have a 'lite' or 'standard' sheet type. "
            "'lite' — the default sheet type for most exams. "
            "'standard' — an alternate sheet format (scanner-form-b). "
            "The sheet type determines which scanner route is loaded in the Vue WebView. "
            "Sheet type is set during exam creation or editing."
        ),
        "metadata": {"category": "mobile-app", "title": "Exams Tab: Sheet Types (Lite vs Standard)"},
    },
    {
        "content": (
            "ExamScanify Classes Tab. "
            "Teachers create and manage class sections. "
            "Each class has: section name and grade level. "
            "Tap a class card to open its student list. "
            "Student management: add, edit, delete students per class. "
            "Each student has a unique student code used for auto-detection during scanning. "
            "Supports bulk class deletion via long-press selection mode. "
            "Classes sync to Supabase cloud storage."
        ),
        "metadata": {"category": "mobile-app", "title": "Classes Tab"},
    },
    {
        "content": (
            "ExamScanify AI Exam Generator (Creator Tab). "
            "Inputs: Subject (from list or custom), Topic (select from list / type manually / upload document), "
            "Item count (10, 20, 30, 40, or 50 items), Exam format (MDAT or Classic HOTS). "
            "Cost system: Generation costs Credits — cost scales with item count and topic length. "
            "New users receive a welcome bonus of Credits on first use. "
            "Credits balance shown as a floating badge (top-right). "
            "The generator calls the ExamScanify backend API with a Supabase JWT auth token."
        ),
        "metadata": {"category": "mobile-app", "title": "AI Exam Generator Tab (Creator)"},
    },
    {
        "content": (
            "ExamScanify AI Credits system. "
            "Credits are the in-app currency for AI Exam Generation. "
            "Credits are consumed per generation; cost is based on item count and topic length surcharges. "
            "Credits can be purchased in the Credits Store (in-app). "
            "A welcome bonus is granted to new users on first use of the AI generator. "
            "Premium users and free users both use Credits for AI generation — Credits are separate from Premium status."
        ),
        "metadata": {"category": "mobile-app", "title": "AI Credits System"},
    },
    {
        "content": (
            "ExamScanify AI Generation flow (Creator Tab): "
            "1. Teacher selects subject, topic, item count, and exam format. "
            "2. App calls backend API (Gemini AI) with Supabase JWT token. "
            "3. AI returns: exam title, questions, answer choices with point values. "
            "4. Choices are shuffled (Fisher-Yates) and re-labeled (a/b/c/d). "
            "5. Answer key is built automatically from the AI response. "
            "6. Exam is saved to local SQLite database. "
            "7. Teacher is redirected to the Exams tab to view the generated exam items."
        ),
        "metadata": {"category": "mobile-app", "title": "AI Generation Flow"},
    },
    {
        "content": (
            "ExamScanify MDAT vs Classic HOTS exam formats: "
            "MDAT (Modified Difficulty-Adjusted Test): "
            "Each answer choice (A, B, C, D) has a different point value. Rubric-based scoring. "
            "Stored as a weights map: {1: {'A': 3, 'B': 2, 'C': 1, 'D': 0}}. "
            "This is the standard format used in DepEd assessments. "
            "Classic HOTS: Only one correct answer per item. Each correct answer = 1 point. "
            "Stored as: {1: 'A', 2: 'C', ...}."
        ),
        "metadata": {"category": "mobile-app", "title": "MDAT vs Classic HOTS Exam Formats"},
    },
    {
        "content": (
            "ExamScanify Account Tab: Membership Status section. "
            "Displays whether the user has a Free Account or Premium Pass (Active). "
            "Premium users see: 'Premium Pass Active', expiry date (e.g., 'Valid until: July 20, 2027'), gold gradient card. "
            "Free users see: upgrade CTA with 'Remove all ads and get an uninterrupted scanning experience today.' "
            "Tapping the card for free users opens the ScannerStore for upgrading."
        ),
        "metadata": {"category": "mobile-app", "title": "Account Tab: Membership Status"},
    },
    {
        "content": (
            "ExamScanify Account Tab sections and settings: "
            "Account Settings: Credits Store, Privacy & Security, Terms & Conditions. "
            "Data Management: Web Console (opens WebConsoleModal), Clean Up Scanned Photos. "
            "Support & Info: Help Center, Ask Scanify AI Agent (BETA chatbot), Submit a Ticket, Rate the App (Google Play), Visit Website, How to Use (Tutorial), App Version. "
            "Danger Zone: Delete Account (wipes all data). "
            "Session: Sign Out."
        ),
        "metadata": {"category": "mobile-app", "title": "Account Tab: All Settings"},
    },
    {
        "content": (
            "ExamScanify Account Tab: AI Agent (Ask Scanify AI Agent). "
            "A BETA feature accessible from the Account tab under Support & Info. "
            "Opens AiAgentModal — a streaming AI chatbot powered by the ExamScanify RAG microservice. "
            "The chatbot can answer questions about ExamScanify features, usage, pricing, and scanning. "
            "Supports markdown rendering in responses. "
            "Uses SSE (Server-Sent Events) for streaming responses."
        ),
        "metadata": {"category": "mobile-app", "title": "Account Tab: Ask Scanify AI Agent (BETA)"},
    },
    {
        "content": (
            "ExamScanify authentication: "
            "Uses Supabase for Google OAuth login. "
            "Teachers sign in with their Google account via supabase.auth.signInWithOAuth (provider: 'google'). "
            "Auth state is managed by UserContext throughout the app. "
            "On logout: Google sign-out, Supabase sign-out, AsyncStorage cleared (userData, userToken, googleIdToken, EXAMS_LIST). "
            "Before sign-out, data is automatically synced to cloud to prevent data loss."
        ),
        "metadata": {"category": "mobile-app", "title": "Authentication & Sign-Out Flow"},
    },
    {
        "content": (
            "ExamScanify local database: "
            "Uses expo-sqlite (SQLite) stored on-device. "
            "Database name: exams_{userId}.db (sanitized UID). "
            "Tables: exams, students, classes, assessments, exam_results. "
            "On account deletion: database is closed, deleted from device, and all scan photos are also deleted. "
            "Answer keys are AES-encrypted before being stored in the exams table."
        ),
        "metadata": {"category": "mobile-app", "title": "Local Database (SQLite)"},
    },
    {
        "content": (
            "ExamScanify cloud sync from mobile: "
            "syncService.syncData(userId) pushes SQLite data to Supabase. "
            "Collections synced: classes, students, exams, exam_results, assessments. "
            "Sync happens automatically on app open and optionally on sign-out. "
            "Last sync time is stored and displayed in the Account tab. "
            "Requires internet connection. Sync errors are shown as toast notifications."
        ),
        "metadata": {"category": "mobile-app", "title": "Cloud Sync from Mobile App"},
    },
    {
        "content": (
            "ExamScanify Web Console Modal (in-app). "
            "Accessible from Account > Data Management > Web Console. "
            "Opens a WebConsoleModal inside the app. "
            "Allows teachers to access the web console features without leaving the app. "
            "Full web console is also available at console.examscanify.com on desktop."
        ),
        "metadata": {"category": "mobile-app", "title": "Web Console Modal (In-App)"},
    },
    {
        "content": (
            "ExamScanify Tutorial system. "
            "First-time users are shown a TutorialModal on the Scanner tab. "
            "After tutorial completion, QuickTips are shown once per session. "
            "Tutorial can be replayed from Account > Support > How to Use. "
            "Tutorial completion state is stored in AsyncStorage under TUTORIAL_STORAGE_KEY."
        ),
        "metadata": {"category": "mobile-app", "title": "Tutorial & Quick Tips"},
    },
    {
        "content": (
            "ExamScanify app version and technical details: "
            "Framework: React Native with Expo (Expo Router). "
            "Platform: Android (primary). "
            "Package name: com.driftapps.scanify. "
            "Scanner engine: Vue.js app compiled to Android assets, using OpenCV.js for computer vision. "
            "State management: React Context (UserContext, TutorialContext). "
            "App version is displayed in Account tab under Support & Info."
        ),
        "metadata": {"category": "mobile-app", "title": "App Technical Details"},
    },

    # ─────────────────────────────────────────────
    # BACKEND
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify backend tech stack: "
            "Node.js server running on port 3001. "
            "Backend API base URL: https://api.examscanify.com. "
            "Primary database: Supabase (PostgreSQL). "
            "Image storage: Cloudinary. "
            "AI generation: Google Gemini API. "
            "Email service: Resend API. "
            "Auth: Supabase (Google OAuth). "
            "Purchase verification: Google Play Developer API. "
            "Legacy: Firebase (service account for firebase-adminsdk)."
        ),
        "metadata": {"category": "backend", "title": "Backend Tech Stack"},
    },
    {
        "content": (
            "ExamScanify Supabase configuration: "
            "Project URL: https://jojkggayoiqrwzhmudxt.supabase.co. "
            "Primary database and authentication provider. "
            "Supabase tables used: users, classes, students, exams, exam_results, assessments, web_sync_pins. "
            "Row-level security (RLS) enforced on all tables. "
            "JWT tokens from Supabase are used to authenticate all backend API calls. "
            "premiumExpiry stored in users table as Unix timestamp."
        ),
        "metadata": {"category": "backend", "title": "Supabase Database & Auth"},
    },
    {
        "content": (
            "ExamScanify backend: Cloud Sync API. "
            "Endpoint: POST /api/sync/:pin/consume. "
            "Requires Supabase JWT bearer token in Authorization header. "
            "The endpoint validates the 6-character PIN against the web_sync_pins table, "
            "verifies the PIN belongs to the authenticated user, "
            "returns the encrypted+zipped backup file (binary), "
            "and deletes the PIN atomically after consumption (one-time use). "
            "Response: binary .zip file containing backup.dat (AES-encrypted JSON)."
        ),
        "metadata": {"category": "backend", "title": "Backend: Cloud Sync API Endpoint"},
    },
    {
        "content": (
            "ExamScanify PIN-based sync mechanism: "
            "The teacher generates a 6-character alphanumeric PIN from the mobile app. "
            "The PIN is stored in Supabase table web_sync_pins with the userId. "
            "The web console prompts for this PIN, validates it against the authenticated user's account, "
            "calls the /api/sync/:pin/consume endpoint to atomically fetch-and-delete the data. "
            "This prevents replay attacks — each PIN can only be consumed once."
        ),
        "metadata": {"category": "backend", "title": "Backend: PIN-Based Sync Flow"},
    },
    {
        "content": (
            "ExamScanify data encryption for sync: "
            "Data is AES-256 encrypted using CryptoJS before transmission. "
            "Encryption key: NEXT_PUBLIC_SYNC_SECRET_KEY (first 32 characters). "
            "IV: NEXT_PUBLIC_SYNC_IV (16-character string). "
            "Encrypted data is then zipped (JSZip) into a .zip file containing backup.dat. "
            "Decryption on web console: unzip → decrypt with same key/IV → parse JSON."
        ),
        "metadata": {"category": "backend", "title": "Backend: AES Encryption & Zip"},
    },
    {
        "content": (
            "ExamScanify Cloudinary integration: "
            "Used for storing scanned exam images uploaded from the mobile app. "
            "Cloudinary cloud name: dhj7xszkh. "
            "Images are uploaded after successful scans for cloud backup. "
            "The Clean Up Scanned Photos feature (Account tab) removes locally stored scan images from the device."
        ),
        "metadata": {"category": "backend", "title": "Backend: Cloudinary Image Storage"},
    },
    {
        "content": (
            "ExamScanify Google Play purchase verification: "
            "A dedicated Google Play Developer service account is used to verify in-app purchases. "
            "Service account email: google-play-android-developer@exam-scanify.iam.gserviceaccount.com. "
            "Google Play package name: com.driftapps.scanify. "
            "Premium Pass purchases are verified server-side using the Google Play Developer API. "
            "On successful verification, premiumExpiry is updated in the Supabase users table."
        ),
        "metadata": {"category": "backend", "title": "Backend: Google Play Purchase Verification"},
    },
    {
        "content": (
            "ExamScanify Gemini AI integration: "
            "Backend uses Google Gemini API (GEMINI_API_KEY) for AI Exam Generation. "
            "The mobile app calls the backend with a Supabase JWT token; the backend calls Gemini. "
            "Gemini generates MDAT or Classic HOTS exam questions, choices, and point values. "
            "Token usage (promptTokenCount, candidatesTokenCount, totalTokenCount) is logged for cost analysis. "
            "The backend enforces credit deduction before calling Gemini."
        ),
        "metadata": {"category": "backend", "title": "Backend: Gemini AI Exam Generation"},
    },
    {
        "content": (
            "ExamScanify Resend email service: "
            "RESEND_API_KEY is configured on the backend. "
            "Used for sending transactional emails such as ambassador activation links and notifications. "
            "Email sender domain: examscanify.com."
        ),
        "metadata": {"category": "backend", "title": "Backend: Resend Email Service"},
    },
    {
        "content": (
            "ExamScanify backend CRON jobs: "
            "Scheduled tasks are secured with CRON_SECRET (value: 3x4mSc4n1fy_Cr0n_S3cr3t_2026). "
            "CRON jobs handle scheduled cleanup and maintenance tasks (e.g., expired PIN cleanup, data housekeeping)."
        ),
        "metadata": {"category": "backend", "title": "Backend: CRON Jobs"},
    },
    {
        "content": (
            "ExamScanify Premium status check: "
            "Premium expiry is stored in Supabase users table as premiumExpiry (Unix timestamp in milliseconds). "
            "The mobile app checks: expiry > Date.now() to determine if premium is active. "
            "The web console checks: expiry > Date.now() on login. "
            "Premium status controls: ad removal, realtime cloud sync access, no scanning limit. "
            "Purchase is one-time annual — does not auto-renew."
        ),
        "metadata": {"category": "backend", "title": "Backend: Premium Status & Expiry Logic"},
    },
    {
        "content": (
            "ExamScanify Firebase integration (legacy): "
            "Firebase service account (project: exam-scanify) is configured on the backend. "
            "Firebase project ID: exam-scanify. "
            "Firebase Admin SDK service account: firebase-adminsdk-fbsvc@exam-scanify.iam.gserviceaccount.com. "
            "Firebase is used for legacy features; Supabase is the primary auth and database."
        ),
        "metadata": {"category": "backend", "title": "Backend: Firebase (Legacy)"},
    },
    {
        "content": (
            "ExamScanify RAG microservice (AI Agent backend): "
            "A separate FastAPI Python microservice powers the Ask Scanify AI Agent chatbot. "
            "Deployed on Render. "
            "Architecture: LangGraph-based RAG pipeline. "
            "Vector store: FAISS for knowledge retrieval. "
            "LLM: Groq (fast inference). "
            "Embeddings: HuggingFace sentence transformers. "
            "Knowledge base: curated chunks in chunks.py (this file). "
            "Supports SSE streaming for real-time response delivery. "
            "Rate limiting: Redis-backed, 20 requests per session."
        ),
        "metadata": {"category": "backend", "title": "RAG Microservice (AI Agent Backend)"},
    },
    {
        "content": (
            "ExamScanify RAG microservice app structure: "
            "app/knowledge/chunks.py — static knowledge base (this file). "
            "app/retriever/ — FAISS vector store retrieval logic. "
            "app/graph/ — LangGraph pipeline definition. "
            "app/memory/ — conversation memory management. "
            "app/routers/ — FastAPI route handlers. "
            "app/config.py — configuration and environment variables."
        ),
        "metadata": {"category": "backend", "title": "RAG Microservice Structure"},
    },

    # ─────────────────────────────────────────────
    # WEB CONSOLE
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify Web Console overview: "
            "Available at https://console.examscanify.com. "
            "A Next.js web application where teachers log in to manage classes, review exam records, "
            "and export comprehensive performance analytics — all in one place. "
            "Requires Google login via Supabase OAuth. "
            "Synced data is loaded from mobile app either via 6-character PIN or cloud auto-fetch (Premium)."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Overview"},
    },
    {
        "content": (
            "ExamScanify Web Console authentication: "
            "Teachers sign in with Google via Supabase OAuth. "
            "Login calls supabase.auth.signInWithOAuth(provider: 'google'). "
            "After login, redirected to /auth/callback?next=/console. "
            "Session state is managed with supabase.auth.onAuthStateChange(). "
            "Auth loading state shown with a spinner while session is verified."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Google Auth"},
    },
    {
        "content": (
            "ExamScanify Web Console Sync Method 1: PIN-based sync. "
            "Teacher generates a 6-character PIN from the mobile app (Account > Web Console). "
            "On the web console, teacher enters the PIN in the SyncLogin or SyncModal. "
            "The web console calls POST /api/sync/:pin/consume with the Supabase JWT token. "
            "Response: binary zip → unzip → AES-decrypt → parse JSON → load dashboard. "
            "PIN is single-use and deleted atomically after consumption."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Sync via PIN"},
    },
    {
        "content": (
            "ExamScanify Web Console Sync Method 2: Cloud auto-fetch (all users). "
            "On login, the web console automatically fetches data from Supabase for all users. "
            "Fetches from collections: classes, students, exams, exam_results, assessments. "
            "Data is filtered by userId. "
            "Exam fields are mapped: exam_name = exam_title, type = topic, item_count = itemCount, mdat_items = items. "
            "Premium users get realtime sync; free users also get auto-fetch on login."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Cloud Auto-Fetch"},
    },
    {
        "content": (
            "ExamScanify Web Console data persistence: "
            "Synced data is saved to localStorage with user UID as key: "
            "examscanify_synced_data, examscanify_last_sync, examscanify_sync_uid. "
            "On page reload, data is loaded from localStorage if the UID matches the current session. "
            "Data from a different user session is cleared automatically to prevent cross-account data leakage. "
            "Data is also saved to Dexie (IndexedDB) via dataService.saveBulkData() for offline access."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Data Persistence"},
    },
    {
        "content": (
            "ExamScanify Web Console data staleness: "
            "Synced data is checked for staleness every 30 seconds. "
            "Data is marked stale if more than 30 minutes have passed since last sync. "
            "A visual stale indicator is shown in the dashboard when data is stale. "
            "Teachers can trigger a manual re-sync via the SyncModal (new sync button)."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Staleness Indicator"},
    },
    {
        "content": (
            "ExamScanify Web Console Dashboard views: "
            "The dashboard shows synced data in two tabs: "
            "1. Classes tab — shows all class sections with their enrolled students. "
            "2. Exams tab — shows all exams with result summaries. "
            "Header shows: user avatar, email, premium badge (if applicable), isSyncing spinner, and new sync button. "
            "Footer included at the bottom of the dashboard."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Dashboard Tabs"},
    },
    {
        "content": (
            "ExamScanify Web Console: Classes & Students view. "
            "Displays all class sections synced from the mobile app. "
            "Each class shows the section name, grade level, and enrolled student count. "
            "Expand a class to see the full student roster with student names and codes."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Classes & Students"},
    },
    {
        "content": (
            "ExamScanify Web Console: Exams & Results view. "
            "Lists all exams with: exam name, subject, item count, type (Classic/MDAT). "
            "Expand an exam to see per-student scores. "
            "Exam Scores view shows: student name, score, percentage, and scanned answers per student. "
            "Overall Summary: aggregated score statistics across all students. "
            "Performance by Class: compares average scores across different class sections."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Exams, Scores & Summary"},
    },
    {
        "content": (
            "ExamScanify Web Console: Item Analysis view. "
            "Shows per-question answer distribution for each exam. "
            "For each item: displays how many students chose each answer option (A, B, C, D). "
            "Distractor analysis: identifies which wrong answers are most commonly selected. "
            "Helps teachers understand class-wide misconceptions and adjust instruction."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Item Analysis"},
    },
    {
        "content": (
            "ExamScanify Web Console: Download Answer Sheets. "
            "Teachers can generate and download printable answer sheets directly from the web console. "
            "Answer sheets are pre-filled with student names, class codes, and unique student IDs. "
            "Layout: 6 students per page. "
            "The downloaded sheets can be printed and distributed to students before an exam."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Download Answer Sheets"},
    },
    {
        "content": (
            "ExamScanify Web Console auto-slider (landing page section): "
            "The landing page at examscanify.com includes an interactive Web Console demo section. "
            "It shows 8 rotating screenshot sections with a sidebar nav: "
            "Classes & Students, Students List, Exams & Results, Exam Scores, Overall Summary, "
            "Performance by Class, Item Analysis, Download Answer Sheets. "
            "Screenshots auto-advance every 3 seconds; clicking a nav item pauses auto-advance. "
            "Displayed in a macOS-style browser window mockup at console.examscanify.com."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Demo (Landing Page)"},
    },
    {
        "content": (
            "ExamScanify Web Console: Dexie IndexedDB integration. "
            "After syncing, all data is also persisted to Dexie (IndexedDB) via dataService.saveBulkData(userId, results). "
            "This enables offline access to synced data in the browser without re-fetching. "
            "The scanner WebView in-app can also access this Dexie data for cross-feature consistency."
        ),
        "metadata": {"category": "web-console", "title": "Web Console: Dexie IndexedDB"},
    },
]
