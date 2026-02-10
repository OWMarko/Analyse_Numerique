static double max_abs_error(
    double t0, double t1, int n,
    const std::vector<double>& u_num
) {
    const double h = (t1 - t0) / static_cast<double>(n);
    double emax = 0.0;
    for (int k = 0; k <= n; ++k) {
        const double t = t0 + k * h;
        emax = std::max(emax, std::abs(u_exact(t) - u_num[k]));
    }
    return emax;
}
