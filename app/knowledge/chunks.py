"""
ExamScanify Knowledge Base
~70 curated chunks across 4 categories:
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
            "Teachers can grade unlimited exams for free or unlock the Premium Pass for a low annual fee. "
            "It is designed specifically for the Philippine educational system and DepEd curriculums."
        ),
        "metadata": {"category": "landing", "title": "ExamScanify Overview"},
    },
    {
        "content": (
            "ExamScanify's Unified Smart Detection means one scanner handles all your exams automatically. "
            "The app identifies the exam type and the student from dedicated codes printed on the answer sheet — "
            "no manual sorting, no need to select the correct exam before scanning. "
            "You can scan a whole stack of different exams in one session without changing any settings."
        ),
        "metadata": {"category": "landing", "title": "Unified Smart Detection"},
    },
    {
        "content": (
            "ExamScanify securely syncs student names, codes, scores, and exam data to an encrypted cloud infrastructure. "
            "This allows teachers to access their data from any device or from the ExamScanify Web Console at console.examscanify.com. "
            "Data is protected with industry-standard encryption."
        ),
        "metadata": {"category": "landing", "title": "Secured Cloud Storage"},
    },
    {
        "content": (
            "ExamScanify provides detailed per-question analytics through its Item Analysis feature. "
            "Teachers can view answer distribution for each question — seeing exactly which choices students selected — "
            "and identify which questions students found most challenging. "
            "This helps educators improve future exams and teaching strategies."
        ),
        "metadata": {"category": "landing", "title": "Item Analysis Feature"},
    },
    {
        "content": (
            "ExamScanify's Class Management feature lets teachers organize students by class or section. "
            "Teachers can track student progress over time, manage multiple sections, "
            "and view per-class analytics. This makes it easy to compare performance across different groups."
        ),
        "metadata": {"category": "landing", "title": "Class Management"},
    },
    {
        "content": (
            "ExamScanify can generate professional Excel (.xlsx) export files containing student scores, "
            "percentages, rankings, and analytics for any exam. "
            "Teachers can share the file via email, save it to cloud storage (Google Drive, OneDrive), "
            "or transfer it to a computer. To export, open an exam and tap the Share icon."
        ),
        "metadata": {"category": "landing", "title": "Excel Export"},
    },
    {
        "content": (
            "ExamScanify is designed to handle all core scanning and grading tasks on-device. "
            "Teachers can manage student records, view analytics, and grade exams locally without internet. "
            "When connectivity is available, data syncs to the cloud automatically. "
            "This offline-first design ensures the app works reliably in areas with poor connectivity."
        ),
        "metadata": {"category": "landing", "title": "Offline Usage"},
    },
    {
        "content": (
            "The AI Exam Generator in ExamScanify lets teachers instantly create high-quality exam questions. "
            "Specify your subject and topic, and the AI automatically generates questions, answer choices, "
            "and populates the answer key in seconds. "
            "The generator supports MDAT (Multidimensional Assessment Tool) format and Classic (HOTS) format. "
            "It is powered by Gemini AI and supports all major DepEd subjects."
        ),
        "metadata": {"category": "landing", "title": "AI Exam Generator Feature"},
    },
    {
        "content": (
            "ExamScanify pricing: The Free tier is completely free forever with unlimited scanning. "
            "Free users can unlock additional scanning sessions by completing a brief interaction when prompted. "
            "The Premium Pass costs ₱299 per year (approximately $5 USD) and provides completely uninterrupted, "
            "seamless scanning experience with priority access to all features including the AI Exam Generator. "
            "There are no monthly fees — only a single annual payment."
        ),
        "metadata": {"category": "landing", "title": "Pricing — Free and Premium"},
    },
    {
        "content": (
            "Spark Credits are the in-app currency used for AI Exam Generation in ExamScanify. "
            "Each AI exam generation costs Spark Credits based on: a base cost of 5 credits, "
            "plus 0.55 credits per exam item (rounded up), plus a surcharge for longer topic content. "
            "Credits are deducted before generation and refunded automatically if generation fails. "
            "Premium Pass users receive more credits than Free users."
        ),
        "metadata": {"category": "landing", "title": "Spark Credits System"},
    },
    {
        "content": (
            "FAQ: How does scanning work? "
            "ExamScanify uses OpenCV technology to detect 6 black square markers on the answer sheet corners and edges. "
            "Once all 6 markers are detected (shown as green indicators on screen), "
            "the app automatically captures the image. "
            "It then detects which bubbles are shaded and calculates scores in real-time using the stored answer key."
        ),
        "metadata": {"category": "landing", "title": "FAQ — How Scanning Works"},
    },
    {
        "content": (
            "FAQ: What is the difference between Classic mode and MDAT mode? "
            "Classic mode uses binary right/wrong scoring where each correct answer gets 1 point. "
            "MDAT (Multidimensional Assessment Tool) mode allows different point values per answer choice "
            "(A=3 points, B=2 points, C=1 point, D=0 points), enabling partial credit and nuanced assessment. "
            "MDAT is the DepEd-recommended format for Philippine schools."
        ),
        "metadata": {"category": "landing", "title": "FAQ — MDAT vs Classic Mode"},
    },
    {
        "content": (
            "FAQ: Is student data safe in ExamScanify? "
            "Yes. All student names, codes, and scores are securely synced to an encrypted cloud infrastructure. "
            "The app uses industry-standard encryption for all data in transit and at rest. "
            "Data is safely backed up and accessible only by the teacher who owns it."
        ),
        "metadata": {"category": "landing", "title": "FAQ — Data Safety"},
    },
    {
        "content": (
            "FAQ: Do I need to select the exam before scanning? "
            "No. Unlike competitors that use generic answer sheets, ExamScanify uses dedicated sheets "
            "with built-in exam codes and student codes. "
            "The unified scanner automatically identifies which exam and which student each sheet belongs to. "
            "You can scan a mixed stack of different exams without changing any settings."
        ),
        "metadata": {"category": "landing", "title": "FAQ — No Pre-selection Needed"},
    },
    {
        "content": (
            "FAQ: Is scanning really unlimited in ExamScanify? "
            "Yes. All users — Free and Premium — can scan unlimited answer sheets. "
            "Free users may occasionally need to complete a brief interaction (e.g., watch a short ad) to unlock more sessions. "
            "Premium Pass users ($5/year, ₱299) have a completely seamless, uninterrupted experience with no interruptions."
        ),
        "metadata": {"category": "landing", "title": "FAQ — Unlimited Scanning"},
    },
    {
        "content": (
            "ExamScanify How It Works: Step 1 — Create your exam in the app (or use AI generation). "
            "Step 2 — Print the MDAT answer sheets. Each sheet has unique codes for the exam and student. "
            "Step 3 — Students take the exam and shade their answers. "
            "Step 4 — Teacher scans each sheet using the ExamScanify camera. "
            "Step 5 — Scores are instantly calculated and saved. Analytics are available immediately."
        ),
        "metadata": {"category": "landing", "title": "How It Works"},
    },
    {
        "content": (
            "ExamScanify is available as a free download on the Google Play Store. "
            "Search for 'ExamScanify' or find it at: "
            "https://play.google.com/store/apps/details?id=com.driftapps.scanify "
            "The app is developed by Drift Apps, a Philippine-based mobile app studio."
        ),
        "metadata": {"category": "landing", "title": "Download and Availability"},
    },
    {
        "content": (
            "ExamScanify supports printable answer sheet outputs. "
            "Teachers can generate and print MDAT-format answer sheets directly from the app. "
            "Each sheet includes: the exam code, student code, bubble grid, and the 6 black detection markers "
            "required for the OpenCV scanning algorithm."
        ),
        "metadata": {"category": "landing", "title": "Printable Answer Sheets"},
    },

    # ─────────────────────────────────────────────
    # MOBILE APP INTERNALS
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify's scanning technology uses OpenCV computer vision to locate 6 black square fiducial markers "
            "positioned at the four corners and two midpoints of the answer sheet. "
            "The markers must all be visible and detected (shown as green squares) before the capture triggers. "
            "This ensures perspective correction and accurate bubble grid alignment regardless of camera angle."
        ),
        "metadata": {"category": "mobile-app", "title": "OpenCV 6-Marker Detection"},
    },
    {
        "content": (
            "Bubble detection in ExamScanify: After marker detection and perspective transformation, "
            "the app maps the expected bubble grid positions and measures the fill percentage of each circle. "
            "A bubble exceeding a configurable fill threshold is marked as shaded. "
            "The detected shaded bubbles are compared against the stored answer key to compute scores."
        ),
        "metadata": {"category": "mobile-app", "title": "Bubble Detection Algorithm"},
    },
    {
        "content": (
            "MDAT mode scoring in ExamScanify: "
            "Choice A is always worth 3 points (most correct), "
            "Choice B is worth 2 points (partially correct), "
            "Choice C is worth 1 point (minimally correct), "
            "Choice D is worth 0 points (incorrect). "
            "This scoring system allows teachers to reward partial understanding "
            "rather than binary right/wrong grading. "
            "The correct answer is always placed in Choice A by the AI generator."
        ),
        "metadata": {"category": "mobile-app", "title": "MDAT Scoring System"},
    },
    {
        "content": (
            "Classic (HOTS) mode in ExamScanify uses binary scoring: "
            "one correct answer (Choice A, marked is_correct=true) worth 1 point, "
            "three distractors worth 0 points. "
            "Questions target Higher-Order Thinking Skills (HOTS) aligned with Bloom's Taxonomy: "
            "Analyzing, Evaluating, and Creating. "
            "This is DepEd's recommended format for critical thinking assessment."
        ),
        "metadata": {"category": "mobile-app", "title": "Classic HOTS Mode"},
    },
    {
        "content": (
            "ExamScanify's AI Exam Generator supports all major DepEd subjects: "
            "Filipino, English, Mathematics, Science, AP (Araling Panlipunan), EsP, "
            "Music, Arts, Physical Education, Health, EPP, TLE, "
            "Oral Communication, Reading and Writing, General Mathematics, "
            "Statistics and Probability, Earth and Life Science, Physical Science, "
            "and Senior High School strands: STEM, ABM, HUMSS, TVL."
        ),
        "metadata": {"category": "mobile-app", "title": "Supported Subjects for AI Generator"},
    },
    {
        "content": (
            "The AI Exam Generator workflow: The teacher selects a subject, enters a topic or pastes reference material, "
            "and chooses the number of items (10, 20, 30, 40, or 50). "
            "The app calls the ExamScanify backend API which uses Gemini AI with a structured JSON schema "
            "to generate either MDAT or Classic exam items in real-time. "
            "The generated exam with populated answer key is immediately usable."
        ),
        "metadata": {"category": "mobile-app", "title": "AI Generator Workflow"},
    },
    {
        "content": (
            "ExamScanify uses Dexie.js as its client-side database for offline-first storage. "
            "All exams, students, classes, and scores are stored locally in IndexedDB via Dexie.js. "
            "When internet is available, data is synced to Supabase cloud storage. "
            "This architecture ensures the app works fully offline and syncs incrementally (delta sync)."
        ),
        "metadata": {"category": "mobile-app", "title": "Dexie.js Offline-First Architecture"},
    },
    {
        "content": (
            "Student code system in ExamScanify: Each student is assigned a unique numeric code within a class. "
            "This code is printed on the student's answer sheet as a barcode/number pattern. "
            "When the sheet is scanned, the app reads this code to automatically assign the score "
            "to the correct student without any manual selection."
        ),
        "metadata": {"category": "mobile-app", "title": "Student Code System"},
    },
    {
        "content": (
            "Exam code system in ExamScanify: Each exam is assigned a unique identifier that is encoded "
            "into the answer sheet design. When scanning, the app reads this code to know which answer key "
            "to apply, which subject the exam belongs to, and which class the student is in. "
            "This enables the unified scanner to handle mixed stacks of answer sheets."
        ),
        "metadata": {"category": "mobile-app", "title": "Exam Code System"},
    },
    {
        "content": (
            "ExamScanify answer key management: Teachers create an answer key when setting up an exam. "
            "For MDAT exams, each item specifies the point values (A=3, B=2, C=1, D=0). "
            "For Classic exams, each item specifies the single correct answer (A). "
            "Answer keys are stored locally and in the cloud. They can be edited before scanning begins."
        ),
        "metadata": {"category": "mobile-app", "title": "Answer Key Management"},
    },
    {
        "content": (
            "Web sync in ExamScanify: Teachers can sync their data between the mobile app and the web console "
            "using a 6-character PIN code. "
            "The teacher uploads a backup file to Cloudinary from the mobile app, receives a PIN, "
            "and enters that PIN in the web console to download and import the data. "
            "The PIN expires after 5 minutes for security."
        ),
        "metadata": {"category": "mobile-app", "title": "Mobile-to-Web Sync via PIN"},
    },
    {
        "content": (
            "ExamScanify analytics features: "
            "Per-exam: total scores, average, highest, lowest, pass rate, score distribution histogram. "
            "Per-question: answer distribution (how many chose A, B, C, D), difficulty index, discrimination index. "
            "Per-student: exam history, score trends across multiple exams. "
            "Per-class: class average, top performers, at-risk students."
        ),
        "metadata": {"category": "mobile-app", "title": "Analytics Features"},
    },
    {
        "content": (
            "ExamScanify requires an Android device to run. "
            "The app is built with React Native (Expo framework) targeting Android. "
            "Minimum Android version: Android 6.0 (API level 23). "
            "A working camera is required for scanning. "
            "The app package name is: com.driftapps.scanify"
        ),
        "metadata": {"category": "mobile-app", "title": "App Requirements"},
    },
    {
        "content": (
            "The ExamScanify mobile app is built with React Native using the Expo framework. "
            "Key mobile libraries: Expo Camera for scanning, Dexie.js for local storage, "
            "React Navigation for routing. "
            "The app communicates with the ExamScanify backend API at api.examscanify.com "
            "using Firebase Bearer token authentication."
        ),
        "metadata": {"category": "mobile-app", "title": "Mobile App Technology Stack"},
    },

    # ─────────────────────────────────────────────
    # BACKEND / API
    # ─────────────────────────────────────────────
    {
        "content": (
            "ExamScanify backend is built with Express 5 and TypeScript, deployed as serverless functions on Vercel. "
            "The backend API is accessible at https://api.examscanify.com. "
            "It handles: exam generation (Gemini AI), user authentication (Firebase), "
            "data storage (Supabase), file storage (Cloudinary), email (Resend), "
            "and Google Play purchase verification."
        ),
        "metadata": {"category": "backend", "title": "Backend Architecture"},
    },
    {
        "content": (
            "ExamScanify backend uses Firebase Admin SDK for authentication. "
            "All protected API endpoints require a Firebase Bearer token in the Authorization header. "
            "The `requireBearerToken` middleware validates the token and extracts the user UID. "
            "Unauthenticated requests receive a 401 Unauthorized response."
        ),
        "metadata": {"category": "backend", "title": "Firebase Authentication"},
    },
    {
        "content": (
            "Spark Credits in the backend: When a teacher requests AI exam generation, "
            "the backend calculates the credit cost server-side (base: 5 credits + 0.55 per item + length surcharge). "
            "It calls `deduct_credits` Supabase RPC atomically before generation. "
            "If generation fails, `increment_credits` is called to refund the exact amount. "
            "This prevents double-spending and ensures fairness."
        ),
        "metadata": {"category": "backend", "title": "Spark Credits — Backend Logic"},
    },
    {
        "content": (
            "Exam generation API: POST /api/generate-exam "
            "Body: { message (topic/reference), subject, itemCount (10-50), isFilipino (bool), examType ('mdat'|'classic') } "
            "The backend uses Google Gemini 2.5 Flash with structured JSON schema output "
            "(responseSchema) to ensure the AI returns a valid, parseable exam structure. "
            "Tokens used are logged for cost analysis."
        ),
        "metadata": {"category": "backend", "title": "Exam Generation API"},
    },
    {
        "content": (
            "Gemini AI integration in ExamScanify backend: "
            "Uses the @google/generative-ai SDK with model 'gemini-2.5-flash'. "
            "MDAT exams use a strict JSON schema enforcing: exam_title, items[], with each item having "
            "item_no, language, question, tos (knowledge/analysis/application), choices[] with letter and points. "
            "Classic exams use a schema with tos (analyzing/evaluating/creating) and is_correct boolean."
        ),
        "metadata": {"category": "backend", "title": "Gemini AI Schema"},
    },
    {
        "content": (
            "Cloudinary is used in ExamScanify backend for temporary file storage during the web sync process. "
            "When a teacher initiates a web sync from the mobile app, the backup file is uploaded to Cloudinary. "
            "The backend generates a 6-character alphanumeric PIN and stores the Cloudinary URL in Supabase. "
            "The file is immediately deleted after the web console downloads it (atomic consume)."
        ),
        "metadata": {"category": "backend", "title": "Cloudinary File Storage"},
    },
    {
        "content": (
            "Supabase is ExamScanify's primary database. "
            "Key tables: exams (exam data), students (student records), web_sync_pins (temporary sync PINs), "
            "config (dynamic app configuration), and user credits. "
            "The backend uses the Supabase service role key for full database access. "
            "Supabase is also used for pgvector (the RAG knowledge base)."
        ),
        "metadata": {"category": "backend", "title": "Supabase Database"},
    },
    {
        "content": (
            "ExamScanify uses Resend for transactional email sending. "
            "Email use cases: ambassador invitation emails, account notifications. "
            "The backend uses the Resend SDK with the API key configured in environment variables."
        ),
        "metadata": {"category": "backend", "title": "Resend Email Service"},
    },
    {
        "content": (
            "Google Play purchase verification in ExamScanify backend: "
            "Uses the Google Play Developer API via a dedicated service account. "
            "When a teacher purchases the Premium Pass through the Android app, "
            "the backend verifies the purchase token with Google Play "
            "and updates the user's premium status in Supabase."
        ),
        "metadata": {"category": "backend", "title": "Google Play Purchase Verification"},
    },
    {
        "content": (
            "ExamScanify backend CORS policy: Allowed origins include *.examscanify.com, "
            "https://examscanify.com, localhost (all ports), capacitor://, ionic://, file://. "
            "This allows the Android app (Capacitor), web console, and landing page "
            "to all call the API securely."
        ),
        "metadata": {"category": "backend", "title": "Backend CORS Policy"},
    },
    {
        "content": (
            "Delta sync in ExamScanify backend: The GET /api/exams endpoint supports a `since` query parameter "
            "(Unix timestamp in ms). It returns only exams updated after that timestamp. "
            "This reduces data transfer on subsequent syncs — the app only downloads changed records, "
            "not the entire dataset."
        ),
        "metadata": {"category": "backend", "title": "Delta Sync Optimization"},
    },
    {
        "content": (
            "The ExamScanify Ambassador Program: Teachers can apply to become ExamScanify ambassadors. "
            "The backend sends ambassador invitation emails via Resend. "
            "Ambassador routes: POST /api/ambassadors/apply, GET /api/ambassadors. "
            "Ambassador data is stored in Supabase."
        ),
        "metadata": {"category": "backend", "title": "Ambassador Program"},
    },
    {
        "content": (
            "ExamScanify cron job: GET /api/cron/cleanup-syncs runs periodically (scheduled by Vercel). "
            "It cleans up expired web sync PINs — deletes the Cloudinary file and removes the Supabase row "
            "for any PIN older than 5 minutes. The cron endpoint is protected by a CRON_SECRET bearer token."
        ),
        "metadata": {"category": "backend", "title": "Cron Cleanup Job"},
    },

    # ─────────────────────────────────────────────
    # WEB CONSOLE
    # ─────────────────────────────────────────────
    {
        "content": (
            "The ExamScanify Web Console is accessible at https://console.examscanify.com. "
            "It is the browser-based companion to the Android app. "
            "Teachers can log in with the same credentials as the mobile app "
            "and access all their synced data from any computer or tablet."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Overview"},
    },
    {
        "content": (
            "Web Console features: "
            "1) View all students and their scores across all exams. "
            "2) Browse all created exams with detailed item analysis. "
            "3) View analytics dashboards (class averages, score distributions). "
            "4) Sync data from mobile app using the 6-character PIN code. "
            "5) Export data as Excel files. "
            "6) Manage account and subscription status."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Features"},
    },
    {
        "content": (
            "Web Console sync process: "
            "1) Teacher opens ExamScanify mobile app and taps 'Sync to Web'. "
            "2) App uploads backup to cloud and displays a 6-character PIN (e.g., 'XK7P2M'). "
            "3) Teacher goes to console.examscanify.com and enters the PIN. "
            "4) Console downloads and imports the data automatically. "
            "5) PIN expires in 5 minutes and the file is deleted immediately after download."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Sync Process"},
    },
    {
        "content": (
            "The ExamScanify Web Console is built with Next.js 16 and hosted on Netlify. "
            "It is part of the examscanify-landing repository at the /app path. "
            "The console uses Supabase for authentication and data access, "
            "Dexie.js for client-side caching, and the ExamScanify backend API for sync operations."
        ),
        "metadata": {"category": "web-console", "title": "Web Console Technical Stack"},
    },
    {
        "content": (
            "ExamScanify is developed by Drift Apps, a Philippine-based mobile app development studio. "
            "Contact: support@examscanify.com. "
            "Developer website: https://drift-apps.netlify.app/. "
            "The app domain is https://examscanify.com. "
            "The admin/developer contact is founder@driftapps.xyz."
        ),
        "metadata": {"category": "landing", "title": "Developer and Contact Info"},
    },
]
