def get_res(et_1, et_4, et_5):
    return 0.66*et_1 + 0.66*et_4 - 0.66*et_5


e41 = get_res(0.5046561059, 0.320937975, 0.5164154355)
e42 = get_res(e41, 0.2831296686, 0.320937975)
e43 = get_res(e42, 0.2875816114, 0.2831296686)
e44 = get_res(e43, 0.5046561059, 0.2875816114)

y44_hat = 0.007342 * 762.1 + e44

print(y44_hat)