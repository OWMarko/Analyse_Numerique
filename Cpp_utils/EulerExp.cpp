std::vector<double> EulerExp(
    const std::function<double(double,double)>& g,
    double u0, double t0, double t1, int n)
    {
    std::vector<double> u(n + 1);
    u[0] = u0;
    const double h = (t1 - t0) / static_cast<double>(n);

    for (int k = 0; k < n; ++k) {
        const double tk = t0 + k * h;
        u[k + 1] = u[k] + h * g(tk, u[k]);
    }
    return u;
}
