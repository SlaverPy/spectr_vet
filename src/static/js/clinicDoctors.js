// Данные специалистов для каждой клиники
const clinicDoctors = {
    'emerald': [
        {
            name: 'Иванов',
            surname: 'Петр',
            patronymic: 'Сергеевич',
            specialization: 'Хирург',
            experience: 12,
            photo: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Специалист по сложным хирургическим операциям. Автор научных работ по ветеринарной хирургии.'
        },
        {
            name: 'Смирнова',
            surname: 'Ольга',
            patronymic: 'Ивановна',
            specialization: 'Терапевт',
            experience: 8,
            photo: 'https://images.unsplash.com/photo-1594824476967-48c8b964273f?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Опытный терапевт с глубокими знаниями в диагностике и лечении внутренних болезней животных.'
        },
        {
            name: 'Кузнецов',
            surname: 'Андрей',
            patronymic: 'Викторович',
            specialization: 'Стоматолог',
            experience: 15,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Ведущий специалист по стоматологии животных. Проводит сложные стоматологические операции.'
        },
        {
            name: 'Попова',
            surname: 'Мария',
            patronymic: 'Александровна',
            specialization: 'Дерматолог',
            experience: 9,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Специалист по кожным заболеваниям у животных.'
        }
    ],
    'andropov': [
        {
            name: 'Петрова',
            surname: 'Елена',
            patronymic: 'Александровна',
            specialization: 'Дерматолог',
            experience: 10,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Специалист по кожным заболеваниям животных. Использует современные методы диагностики.'
        },
        {
            name: 'Сидоров',
            surname: 'Михаил',
            patronymic: 'Петрович',
            specialization: 'Офтальмолог',
            experience: 7,
            photo: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Эксперт по заболеваниям глаз у животных. Проводит микрохирургические операции.'
        },
        {
            name: 'Козлов',
            surname: 'Алексей',
            patronymic: 'Владимирович',
            specialization: 'Кардиолог',
            experience: 11,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Специалист по заболеваниям сердца у животных.'
        }
    ],
    'lenskaya': [
        {
            name: 'Васильев',
            surname: 'Дмитрий',
            patronymic: 'Николаевич',
            specialization: 'Кардиолог',
            experience: 14,
            photo: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Кардиолог высшей категории. Специализируется на заболеваниях сердечно-сосудистой системы.'
        },
        {
            name: 'Николаева',
            surname: 'Анна',
            patronymic: 'Владимировна',
            specialization: 'Невролог',
            experience: 9,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Невролог с большим опытом работы. Диагностирует и лечит заболевания нервной системы.'
        },
        {
            name: 'Федоров',
            surname: 'Сергей',
            patronymic: 'Игоревич',
            specialization: 'Онколог',
            experience: 11,
            photo: 'https://images.unsplash.com/photo-1594824476967-48c8b964273f?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Онколог, специализирующийся на диагностике и лечении опухолевых заболеваний у животных.'
        },
        {
            name: 'Орлова',
            surname: 'Татьяна',
            patronymic: 'Сергеевна',
            specialization: 'Стоматолог',
            experience: 8,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Специалист по стоматологии животных.'
        },
        {
            name: 'Белов',
            surname: 'Андрей',
            patronymic: 'Игоревич',
            specialization: 'Хирург',
            experience: 13,
            photo: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80',
            description: 'Опытный хирург, специализируется на ортопедических операциях.'
        }
    ]
};

// Тексты для клиник
const clinicTitles = {
    'emerald': 'Изумрудная, 3',
    'andropov': 'Андропова, 15',
    'lenskaya': 'Ленская, 10'
};

// Текущая выбранная клиника
let currentClinic = null;

// Функция для загрузки специалистов
function loadClinicDoctors(clinicId) {
    const container = document.getElementById('clinic-doctors-container');
    const clinicText = document.getElementById('selected-clinic-text');
    const doctors = clinicDoctors[clinicId];

    currentClinic = clinicId;

    // Обновляем текст
    clinicText.innerHTML = `Специалисты клиники: <strong>${clinicTitles[clinicId]}</strong>`;

    if (!doctors || doctors.length === 0) {
        container.innerHTML = `
            <div class="text-center text-muted">
                <i class="bi bi-exclamation-circle display-4 mb-3"></i>
                <p>Специалисты не найдены для выбранной клиники</p>
            </div>
        `;
        return;
    }

    let doctorsHTML = `
        <div class="doctors-scroll-container">
            <div class="doctors-scroll-wrapper">
                <div class="doctors-grid">
    `;

    doctors.forEach(doctor => {
        console.log(doctor.photo)
        doctorsHTML += `
            <div class="doctor-card-wrapper">
                <div class="card h-100 border-0 shadow-sm doctor-card">
                    <img src="${doctor.photo}" 
                         class="card-img-top" 
                         alt="${doctor.surname} ${doctor.name} ${doctor.patronymic}">
                    <div class="card-body">
                        <h5 class="card-title text-green">${doctor.surname} ${doctor.name} ${doctor.patronymic}</h5>
                        <p class="card-text mb-1">
                            <strong>Специализация:</strong> ${doctor.specialization}
                        </p>
                        <p class="card-text">
                            <strong>Стаж:</strong> ${doctor.experience} ${getExperienceWord(doctor.experience)}
                        </p>
                        <p class="card-text small text-muted doctor-description">${doctor.description}</p>
                    </div>
                    <div class="card-footer bg-transparent border-0">
                        <button class="btn btn-outline-success w-100" 
                                onclick="showDoctorDetails('${doctor.surname}', '${doctor.name}', '${doctor.patronymic}', '${doctor.specialization}', ${doctor.experience}, '${doctor.description}')">
                            Подробнее
                        </button>
                    </div>
                </div>
            </div>
        `;
    });

    doctorsHTML += `
                </div>
            </div>
            <button class="scroll-btn scroll-left" onclick="scrollDoctors(-1)">
                <i class="bi bi-chevron-left"></i>
            </button>
            <button class="scroll-btn scroll-right" onclick="scrollDoctors(1)">
                <i class="bi bi-chevron-right"></i>
            </button>
        </div>
    `;

    container.innerHTML = doctorsHTML;

    // Инициализируем кнопки прокрутки
    initScrollButtons();
}

// Функция для прокрутки специалистов
function scrollDoctors(direction) {
    const scrollContainer = document.querySelector('.doctors-scroll-wrapper');
    const scrollAmount = 300; // Шаг прокрутки

    if (scrollContainer) {
        scrollContainer.scrollBy({
            left: direction * scrollAmount,
            behavior: 'smooth'
        });
    }
}

// Инициализация кнопок прокрутки
function initScrollButtons() {
    const scrollWrapper = document.querySelector('.doctors-scroll-wrapper');
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');

    if (!scrollWrapper) return;

    // Проверяем видимость кнопок при прокрутке
    scrollWrapper.addEventListener('scroll', updateScrollButtons);
    updateScrollButtons();

    function updateScrollButtons() {
        if (scrollLeftBtn && scrollRightBtn) {
            const scrollLeft = scrollWrapper.scrollLeft;
            const maxScroll = scrollWrapper.scrollWidth - scrollWrapper.clientWidth;

            scrollLeftBtn.style.display = scrollLeft > 0 ? 'flex' : 'none';
            scrollRightBtn.style.display = scrollLeft < maxScroll - 10 ? 'flex' : 'none';
        }
    }
}

// Функция для правильного склонения слова "год"
function getExperienceWord(years) {
    if (years % 10 === 1 && years % 100 !== 11) return 'год';
    if ([2, 3, 4].includes(years % 10) && ![12, 13, 14].includes(years % 100)) return 'года';
    return 'лет';
}

// Функция для показа деталей специалиста
function showDoctorDetails(surname, name, patronymic, specialization, experience, description) {
    // Можно реализовать модальное окно
    const modalHTML = `
        <div class="modal fade" id="doctorModal" tabindex="-1">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">${surname} ${name} ${patronymic}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <p><strong>Специализация:</strong> ${specialization}</p>
                        <p><strong>Стаж:</strong> ${experience} ${getExperienceWord(experience)}</p>
                        <p><strong>О специалисте:</strong> ${description}</p>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Добавляем модальное окно в DOM и показываем его
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    const modal = new bootstrap.Modal(document.getElementById('doctorModal'));
    modal.show();

    // Удаляем модальное окно после закрытия
    document.getElementById('doctorModal').addEventListener('hidden.bs.modal', function () {
        this.remove();
    });
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function () {
    // Обработчик для аккордеона клиник
    const accordionButtons = document.querySelectorAll('.accordion-button');

    accordionButtons.forEach(button => {
        button.addEventListener('click', function () {
            const clinicId = this.getAttribute('data-clinic-id');
            if (clinicId && clinicId !== currentClinic) {
                loadClinicDoctors(clinicId);
            }
        });
    });

    // Загружаем специалистов для первой клиники по умолчанию
    const firstClinicButton = document.querySelector('.accordion-button[data-clinic-id]');
    if (firstClinicButton) {
        const firstClinicId = firstClinicButton.getAttribute('data-clinic-id');
        loadClinicDoctors(firstClinicId);
    }
});