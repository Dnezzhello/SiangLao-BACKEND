#!/usr/bin/env python3
"""
Test script to diagnose soundfile issues
"""

import os
import sys
import numpy as np

def test_soundfile_import():
    """Test if soundfile can be imported"""
    try:
        import soundfile as sf
        print("✅ soundfile imported successfully")
        print(f"   Version: {sf.__version__}")
        return True
    except ImportError as e:
        print(f"❌ soundfile import failed: {e}")
        return False

def test_libsndfile_availability():
    """Test if libsndfile is available"""
    try:
        import soundfile as sf
        # Try to get libsndfile info
        print("✅ libsndfile available")
        return True
    except Exception as e:
        print(f"❌ libsndfile not available: {e}")
        return False

def test_soundfile_basic_functionality():
    """Test basic soundfile functionality"""
    try:
        import soundfile as sf
        
        # Create a simple test audio signal
        sample_rate = 16000
        duration = 1.0
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio = np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave
        
        # Test file path
        test_file = "/tmp/test_audio.wav"
        
        # Write audio file
        sf.write(test_file, audio, sample_rate)
        print("✅ soundfile write successful")
        
        # Read audio file
        audio_read, sr_read = sf.read(test_file)
        print("✅ soundfile read successful")
        print(f"   Sample rate: {sr_read}")
        print(f"   Duration: {len(audio_read)/sr_read:.2f}s")
        
        # Clean up
        os.remove(test_file)
        
        return True
    except Exception as e:
        print(f"❌ soundfile basic functionality failed: {e}")
        return False

def test_librosa_with_soundfile():
    """Test librosa with soundfile backend"""
    try:
        import librosa
        import soundfile as sf
        
        # Create test audio
        sample_rate = 16000
        duration = 1.0
        t = np.linspace(0, duration, int(sample_rate * duration))
        audio = np.sin(2 * np.pi * 440 * t)
        
        test_file = "/tmp/test_librosa.wav"
        sf.write(test_file, audio, sample_rate)
        
        # Test librosa loading
        audio_librosa, sr_librosa = librosa.load(test_file, sr=sample_rate)
        print("✅ librosa with soundfile backend successful")
        print(f"   Sample rate: {sr_librosa}")
        print(f"   Duration: {len(audio_librosa)/sr_librosa:.2f}s")
        
        # Clean up
        os.remove(test_file)
        
        return True
    except Exception as e:
        print(f"❌ librosa with soundfile backend failed: {e}")
        return False

def main():
    print("🔍 Diagnosing soundfile issues...")
    print("=" * 50)
    
    # Test 1: Import soundfile
    test_soundfile_import()
    
    # Test 2: Check libsndfile availability
    test_libsndfile_availability()
    
    # Test 3: Test basic soundfile functionality
    test_soundfile_basic_functionality()
    
    # Test 4: Test librosa with soundfile
    test_librosa_with_soundfile()
    
    print("=" * 50)
    print("🏁 Diagnosis complete")

if __name__ == "__main__":
    main()