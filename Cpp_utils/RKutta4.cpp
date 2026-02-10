std::vector<double> RKutta4(
    const std::function<double(double,double)>& g,
    double u0, double t0, double t1, int n
) {
    std::vector<double> u(n + 1);
    u[0] = u0;
    const double h = (t1 - t0) / static_cast<double>(n);

    for (int k = 0; k < n; ++k) {
        const double tk = t0 + k * h;
        const double uk = u[k];

        const double k1 = g(tk, uk);
        const double k2 = g(tk + 0.5 * h, uk + 0.5 * h * k1);
        const double k3 = g(tk + 0.5 * h, uk + 0.5 * h * k2);
        const double k4 = g(tk + h,       uk + h * k3);

        u[k + 1] = uk + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4);
    }
    return u;
}
