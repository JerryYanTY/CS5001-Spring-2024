import unittest
from depth import depth


class DepthTesting(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, depth({}))

    def test_2(self):
        self.assertEqual(2, depth({"key1": {
                                    "key3": 34,
                                    "key4": 56
                                },
                                "key2": "fish"
                            }))

    def test_3(self):
        self.assertEqual(3, depth({"key1": {
                                    "key3": {},
                                    "key4": 56
                                },
                                "key2": "fish"
                            }))

    def test_4(self):
        self.assertEqual(4, depth({
                            "key1": {
                                "key2": "value1",
                                "key3": [1, 2, 3]
                            },
                            "key4": {
                                "key5": {
                                    "key6": {
                                        "key8": "fish"
                                    }
                                },
                                "key7": 34
                            }
                        }))

    def test_5(self):
        self.assertEqual(5, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": ''
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }))

    def test_6(self):
        self.assertEqual(6, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": {
                                                        "key10": ''
                                                    }
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }))

    def test_7(self):
        self.assertEqual(7, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": {
                                                        "key10": {
                                                            "key11": ''
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }))

    def test_8(self):
        self.assertEqual(8, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": {
                                                        "key10": {
                                                            "key11": {
                                                                "key12": ''
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }))

    def test_9(self):
        self.assertEqual(9, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": {
                                                        "key10": {
                                                            "key11": {
                                                                "key12": {
                                                                    "key13": ''
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }))

    def test_10(self):
        self.assertEqual(10, depth({
                                    "key1": {
                                        "key2": "value1",
                                        "key3": [1, 2, 3]
                                    },
                                    "key4": {
                                        "key5": {
                                            "key6": {
                                                "key8": {
                                                    "key9": {
                                                        "key10": {
                                                            "key11": {
                                                                "key12": {
                                                                    "key13": {
                                                                        "key14": ''
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        "key7": 34
                                    }
                                }
                                ))


if __name__ == '__main__':
    unittest.main()
