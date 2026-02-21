import time
import os

# --- Dummy Database ---
JOB_DATABASE = [
    {"title": "DevOps Engineer", "skills": ["aws", "docker", "kubernetes"], "location": "Bangalore", "company": "CloudX"},
    {"title": "Python Developer", "skills": ["python", "django", "git"], "location": "Hyderabad", "company": "TechPy"},
    {"title": "Data Scientist", "skills": ["python", "pandas", "ml"], "location": "Pune", "company": "DataMind"},
    {"title": "Cloud Architect", "skills": ["aws", "azure", "terraform"], "location": "Delhi", "company": "SkyNet"},
    {"title": "Backend Engineer", "skills": ["python", "flask", "docker"], "location": "Mumbai", "company": "LinkOps"},
    {"title": "Security Analyst", "skills": ["linux", "networking", "aws"], "location": "Chennai", "company": "SafeNet"}
]

class JobPortal:
    def __init__(self):
        self.user_data = {}
        self.is_logged_in = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # 1. Sign-In Logic
    def sign_in(self):
        print("\n--- 🔐 Welcome to SkillSync Sign-In ---")
        identifier = input("Enter Email or Mobile Number: ").strip()
        if "@" in identifier or (identifier.isdigit() and len(identifier) >= 10):
            print(f"Verifying {identifier}...")
            time.sleep(1)
            self.is_logged_in = True
            return True
        else:
            print("❌ Invalid Email or Mobile format!")
            return False

    # 2. Profile Setup (Manual Entry)
    def create_profile(self):
        print("\n--- 👤 Complete Your Profile ---")
        name = input("Enter Full Name: ")
        skills = input("Enter Skills (comma separated): ").lower().split(",")
        skills = [s.strip() for s in skills]
        
        self.user_data = {"name": name, "skills": skills}
        
        print("\nCreating your account...")
        time.sleep(1.5)
        print(f"✅ Account Created Successfully! Welcome, {name}!")
        time.sleep(1)

    # 3. Search Engine (Pan India)
    def search_jobs(self):
        self.clear_screen()
        print(f"\n--- 🔍 Job Search Dashboard (Pan India) ---")
        print(f"Logged in as: {self.user_data['name']}")
        
        keyword = input("\nEnter Job Keyword or Skill to search: ").lower().strip()
        
        print(f"\nSearching for '{keyword}' across India...")
        time.sleep(1)
        
        matches = []
        for job in JOB_DATABASE:
            # Logic: Match keyword in title OR skills
            if keyword in job['title'].lower() or any(keyword in s for s in job['skills']):
                # Calculate Match score based on user's registered skills
                user_skills = set(self.user_data['skills'])
                job_skills = set(job['skills'])
                common = user_skills.intersection(job_skills)
                match_pct = (len(common) / len(job_skills)) * 100 if job_skills else 0
                
                matches.append({"job": job, "pct": match_pct})

        # Display Results
        if matches:
            print(f"\n🎯 Found {len(matches)} Relevant Jobs:")
            print("-" * 50)
            for m in sorted(matches, key=lambda x: x['pct'], reverse=True):
                j = m['job']
                print(f"🔹 {j['title']} | {j['company']}")
                print(f"   📍 Location: {j['location']}")
                print(f"   📊 Profile Match: {m['pct']:.1f}%")
                print("-" * 50)
        else:
            print(f"❌ No jobs found for '{keyword}'. Try a different keyword like 'Python' or 'AWS'.")

# --- Main Flow ---
def main():
    portal = JobPortal()
    
    # Flow 1: Sign In
    while not portal.is_logged_in:
        if portal.sign_in():
            break
    
    # Flow 2: Profile Creation
    portal.create_profile()
    
    # Flow 3: Search Loop
    while True:
        portal.search_jobs()
        cont = input("\nSearch again? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye! All the best for your job hunt.")
            break

if __name__ == "__main__":
    main()