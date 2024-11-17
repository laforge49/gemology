from pdml import saver, textin, loader
import pathlib


def generate_samples(test_data_path: pathlib.Path, round_trip: bool,
                     round_trip_data_samples: list) -> None:
    i = 0
    for da in round_trip_data_samples:
        i += 1
        ri = str(i).rjust(3, "0")
        to_file_name = "g" + ri + ".pdml"
        to_path = test_data_path / "generated" / to_file_name
        print(to_path)
        st = saver.writer(to_path, da)
        if round_trip:
            cursor: textin.Cursor = textin.cursor_from_string(st)
            da1 = loader.process_input(cursor)
            if da != da1:
                raise Exception("round trip failure on" + str(to_path))


def string_round_trips(directory_path: pathlib.Path) -> None:
    for pdml_path in directory_path.glob("*.pdml"):
        print(pdml_path)
        da = loader.file_reader(pdml_path)
        print(da)
        s = saver.data_to_string(0, da, False)
        print(s)


def test_manual(home_path: pathlib.Path) -> None:
    test_data_path = home_path / pathlib.Path("test data")
    manual_path = test_data_path / "manual"
    print("\nmanual string round trips:\n")
    string_round_trips(manual_path)


def test_generated(home_path: pathlib.Path, round_trip: bool) -> None:

    round_trip_data_samples = ["123", 42, {}, [],
                               [1, 2, 3],
                               [2, [23, False], "ho", {5: 55}],
                               {1: 11, 2: 30},
                               {3: [2, 22]},
                               {3: [2, 22], 4: True},
                               {1: {True: False}, 2: "oh"},
                               {1: {True: False}, 2: "oh", 3: [2, 22], 4: True},
                               {42}, {3, 1, 2}, set()]

    test_data_path = home_path / pathlib.Path("test data")
    generate_samples(test_data_path, round_trip, round_trip_data_samples)
    if round_trip:
        generated_path = test_data_path / "generated"
        print("\ngenerated string round trips:\n")
        string_round_trips(generated_path)


def pdml_tests(home_path: pathlib, round_trip: bool) -> None:
    print("\npdml tests\n")
    textin.test_textin(home_path)
    loader.test_loader(home_path)
    saver.test_write(home_path)
    test_manual(home_path)
    test_generated(home_path, round_trip)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    home_path = pathlib.Path.cwd()
    pdml_tests(home_path, True)
