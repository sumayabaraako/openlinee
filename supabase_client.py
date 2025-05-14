from supabase import create_client, Client

SUPABASE_URL = "https://ouhnlqmgfieejbmmwzke.supabase.co"  
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im91aG5scW1nZmllZWpibW13emtlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUzOTczMjMsImV4cCI6MjA2MDk3MzMyM30.lSBuSgPOXiDwcgJTIshZI-6swLlkQviKqNAZ4vRlICQ"  

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)