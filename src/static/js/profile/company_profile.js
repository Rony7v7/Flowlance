document.getElementById('editProfileButton').addEventListener('click', function() {
    document.getElementById('editProfileModal').classList.remove('hidden');
});

document.getElementById('closeModal').addEventListener('click', function() {
    document.getElementById('editProfileModal').classList.add('hidden');
});