// Load components
document.addEventListener('DOMContentLoaded', function() {
    loadComponent('header-placeholder', 'components/header.html');
    loadComponent('footer-placeholder', 'components/footer.html');
    loadServices();
    // loadDoctors();
    loadReviews();
});

// Function to load HTML components
function loadComponent(elementId, filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            document.getElementById(elementId).innerHTML = data;
        })
        .catch(error => {
            console.error('Error loading component:', error);
        });
}

// Mock data for services
function loadServices() {
    const services = [
        {
            icon: 'bi-heart-pulse',
            title: 'Терапия и диагностика',
            description: 'Комплексное обследование, анализы, УЗИ и рентген',
            price: 'от 1500₽'
        },
        {
            icon: 'bi-scissors',
            title: 'Хирургия',
            description: 'Операции любой сложности на современном оборудовании',
            price: 'от 3000₽'
        },
        {
            icon: 'bi-shield-plus',
            title: 'Вакцинация',
            description: 'Комплексная вакцинация и профилактика заболеваний',
            price: 'от 800₽'
        },
        {
            icon: 'bi-droplet',
            title: 'Стоматология',
            description: 'Лечение и профилактика заболеваний зубов и полости рта',
            price: 'от 2000₽'
        },
        {
            icon: 'bi-scissors',
            title: 'Груминг',
            description: 'Профессиональный уход за шерстью и гигиенические процедуры',
            price: 'от 1200₽'
        },
        {
            icon: 'bi-house',
            title: 'Вызов на дом',
            description: 'Ветеринарная помощь в комфортных домашних условиях',
            price: 'от 2500₽'
        }
    ];

    const servicesContainer = document.querySelector('#services .row.g-4');
    servicesContainer.innerHTML = services.map(service => `
        <div class="col-md-6 col-lg-4">
            <div class="card service-card h-100 border-0 shadow-sm">
                <div class="card-body text-center p-4">
                    <div class="bg-light-green rounded-circle d-inline-flex align-items-center justify-content-center mb-3" style="width: 80px; height: 80px;">
                        <i class="bi ${service.icon} text-green fs-1"></i>
                    </div>
                    <h5 class="card-title fw-bold">${service.title}</h5>
                    <p class="card-text text-muted">${service.description}</p>
                    <span class="text-primary fw-bold">${service.price}</span>
                </div>
            </div>
        </div>
    `).join('');
}

// Mock data for doctors
function loadDoctors() {
    const doctors = [
        {
            image: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            name: 'Мария Иванова',
            position: 'Главный ветеринарный врач',
            experience: 'Стаж: 12 лет'
        },
        {
            image: 'https://images.unsplash.com/photo-1594824476967-48c8b964273f?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            name: 'Алексей Петров',
            position: 'Хирург',
            experience: 'Стаж: 8 лет'
        },
        {
            image: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            name: 'Елена Сидорова',
            position: 'Стоматолог',
            experience: 'Стаж: 6 лет'
        },
        {
            image: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            name: 'Дмитрий Кузнецов',
            position: 'Терапевт',
            experience: 'Стаж: 10 лет'
        }
    ];

    const doctorsContainer = document.querySelector('#doctors .row.g-4');
    doctorsContainer.innerHTML = doctors.map(doctor => `
        <div class="col-md-6 col-lg-3">
            <div class="card doctor-card border-0 h-100">
                <img src="${doctor.image}" class="doctor-img" alt="${doctor.name}">
                <div class="card-body">
                    <h5 class="card-title fw-bold">${doctor.name}</h5>
                    <p class="text-muted">${doctor.position}</p>
                    <p class="small text-muted">${doctor.experience}</p>
                </div>
            </div>
        </div>
    `).join('');
}

// Mock data for reviews
function loadReviews() {
    const reviews = [
        {
            initials: 'ИП',
            name: 'Иван Петров',
            role: 'Владелец кошки',
            text: '"Отличная клиника! Вылечили нашего кота быстро и профессионально. Цены адекватные, врачи внимательные."',
            rating: 5
        },
        {
            initials: 'ЕС',
            name: 'Екатерина Смирнова',
            role: 'Владелец собаки',
            text: '"Очень благодарна врачам за спасение моего лабрадора! Операция прошла успешно, реабилитация быстрая. Спасибо!"',
            rating: 5
        },
        {
            initials: 'АН',
            name: 'Анна Николаева',
            role: 'Владелец попугая',
            text: '"Привозила попугая на обследование. Врач очень аккуратно работала с птицей, всё объяснила. Теперь только к вам!"',
            rating: 4.5
        }
    ];

    const reviewsContainer = document.querySelector('#reviews .row.g-4');
    reviewsContainer.innerHTML = reviews.map(review => `
        <div class="col-lg-4">
            <div class="review-card h-100">
                <div class="d-flex align-items-center mb-3">
                    <div class="bg-primary rounded-circle d-flex align-items-center justify-content-center" style="width: 50px; height: 50px;">
                        <span class="text-white fw-bold">${review.initials}</span>
                    </div>
                    <div class="ms-3">
                        <h6 class="mb-0 fw-bold">${review.name}</h6>
                        <small class="text-muted">${review.role}</small>
                    </div>
                </div>
                <p class="mb-0">${review.text}</p>
                <div class="text-warning mt-2">
                    ${getRatingStars(review.rating)}
                </div>
            </div>
        </div>
    `).join('');
}

function getRatingStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    let stars = '';

    for (let i = 0; i < fullStars; i++) {
        stars += '<i class="bi bi-star-fill"></i>';
    }

    if (hasHalfStar) {
        stars += '<i class="bi bi-star-half"></i>';
    }

    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {
        stars += '<i class="bi bi-star"></i>';
    }

    return stars;
}