css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://resize.elle.fr/original/var/plain_site/storage/images/people/la-vie-des-people/news/carrie-fisher-le-message-d-outre-tombe-de-la-princesse-leia-qui-a-emu-sa-famille-3829301/92306649-1-fre-FR/Carrie-Fisher-le-message-d-outre-tombe-de-la-princesse-Leia-qui-a-emu-sa-famille.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.a.transfermarkt.technology/portrait/header/206746-1599577236.jpg?lm=1">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''