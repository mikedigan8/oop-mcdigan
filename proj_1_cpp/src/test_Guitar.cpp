#include "Guitar.h"
#include "gtest/gtest.h"

using namespace std;
using namespace instrument;

TEST(Guitar, Defaults) {
    Guitar guitar;
    ASSERT_EQ(guitar.getStringCount(),Guitar::DEFAULT_STRING_COUNT);
    ASSERT_EQ(guitar.getStringGauge(),Guitar::DEFAULT_STRING_GAUGE);
    ASSERT_EQ(guitar.getTuning(),Guitar::DEFAULT_TUNING);
    ASSERT_EQ(guitar.getVolume(),Guitar::DEFAULT_VOLUME);
}

TEST(Guitar, BadValues) {
    Guitar guitar;

    int testNumStrings = -1;
    guitar.setStringCount(testNumStrings);
    ASSERT_EQ(guitar.getStringCount(), 0);

    int testVolume = -1;
    guitar.setVolume(testVolume);
    ASSERT_EQ(guitar.getVolume(),0.0);

    testVolume = 11;
    guitar.setVolume(testVolume);
    ASSERT_EQ(guitar.getVolume(),10.0);

    string testTuning = "Z Z Z Z Z Z";
    guitar.setTuning(testTuning);
    ASSERT_EQ(guitar.getTuning(), guitar.DEFAULT_TUNING);

    testTuning = "A B C";
    guitar.setTuning(testTuning);
    ASSERT_EQ(guitar.getTuning(), guitar.DEFAULT_TUNING);
}

TEST(Guitar, Specific) {
    int testStrings = 7;
    int testGauge = 2223;
    string testTuning = "Ab A A A A A A";
    double testVolume = 5.7;
    Guitar guitar(testStrings, testGauge, testTuning, testVolume);

    ASSERT_EQ(guitar.getStringCount(), testStrings);
    ASSERT_EQ(guitar.getStringGauge(), testGauge);
    ASSERT_EQ(guitar.getTuning(), testTuning);
    ASSERT_EQ(guitar.getVolume(), testVolume);

    testStrings = 6;
    testGauge = 2225;
    testTuning = "Ab B C# D Eb F";
    testVolume = 9.9;

    guitar.setStringCount(testStrings);
    guitar.setStringGauge(testGauge);
    guitar.setTuning(testTuning);
    guitar.setVolume(testVolume);

    ASSERT_EQ(guitar.getStringCount(), testStrings);
    ASSERT_EQ(guitar.getStringGauge(), testGauge);
    ASSERT_EQ(guitar.getTuning(), testTuning);
    ASSERT_EQ(guitar.getVolume(), testVolume);
}

int main(int args, char** argv) {
    ::testing::InitGoogleTest(&args, argv);
    return RUN_ALL_TESTS();
}