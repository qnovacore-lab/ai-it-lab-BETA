"""Basit, bellekte çalışan IT ticket yönetim uygulaması."""


def create_ticket(tickets):
    """Kullanıcıdan bilgiler alıp yeni bir ticket oluşturur."""
    title = input("Ticket başlığı: ").strip()
    while not title:
     print("Başlık boş bırakılamaz.")
     title = input("Ticket başlığı: ").strip()

    description = input("Ticket açıklaması: ").strip()
    while not description:
        print("Açıklama Boş Bırakılamaz.")
        description = input("Ticket açıklaması: ").strip()

    if not title or not description:
        print("Başlık ve açıklama boş bırakılamaz.\n")
        return

    print("Öncelik seçenekleri: düşük, orta, yüksek")
    priority = input("Öncelik: ").strip().lower()

    while priority not in ("düşük", "orta", "yüksek"):
        print("Lütfen düşük, orta veya yüksek seçeneklerinden birini girin.")
        priority = input("Öncelik: ").strip().lower()

    ticket = {
        "title": title,
        "description": description,
        "priority": priority,
    }
    tickets.append(ticket)
    print("Ticket oluşturuldu.\n")


def list_tickets(tickets):
    """Oluşturulan ticket'ları listeler."""
    if not tickets:
        print("Henüz oluşturulmuş ticket yok.\n")
        return

    print("\nTicket listesi:")
    for number, ticket in enumerate(tickets, start=1):
        print(f"\n{number}. {ticket['title']}")
        print(f"   Açıklama: {ticket['description']}")
        print(f"   Öncelik: {ticket['priority']}")
    print()


def main():
    """Uygulamanın menüsünü çalıştırır."""
    tickets = []

    while True:
        print("IT Ticket Yönetimi")
        print("1. Ticket oluştur")
        print("2. Ticket'ları listele")
        print("3. Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            create_ticket(tickets)
        elif choice == "2":
            list_tickets(tickets)
        elif choice == "3":
            print("Uygulamadan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.\n")


if __name__ == "__main__":
    main()
