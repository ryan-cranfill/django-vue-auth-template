import session from './session';

export default {
  login(username, password) {
    return session.post('/api/auth/login/', { username, password });
  },
  logout() {
    return session.post('/api/auth/logout/', {});
  },
  createAccount(username, password1, password2, email) {
    return session.post('/api/registration/', { username, password1, password2, email });
  },
  changeAccountPassword(password1, password2) {
    return session.post('/api/auth/password/change/', { password1, password2 });
  },
  sendAccountPasswordResetEmail(email) {
    return session.post('/api/auth/password/reset/', { email });
  },
  resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
    return session.post('/api/auth/password/reset/confirm/', { uid, token, new_password1, new_password2 });
  },
  getAccountDetails() {
    return session.get('/api/auth/user/');
  },
  updateAccountDetails(data) {
    return session.patch('/api/auth/user/', data);
  },
  verifyAccountEmail(key) {
    return session.post('/api/registration/verify-email/', { key });
  },
};
