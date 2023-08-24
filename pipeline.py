from language import summarize
from voice import create_voice
from torch.cuda import empty_cache
from subprocess import run

def get_voice(text, voice_profile):
    # get summary from our model

    summary = summarize(text)
    empty_cache()

    print("***SUMMARY***")
    print(summary)
    print("***SUMMARY***")

    create_voice(summary)
    print("***VOICE CREATED***")

    print(f"***VOICE USED:{voice_profile}")
    run(
        [
            "python", "scripts/voice_conversion.py", 
            "--source_path", "../flask-argon-dashboard/initial.wav", 
            "--decoder_path", f"{voice_profile}/main.pt", 
            "--generated_sample_path", "../flask-argon-dashboard/apps/static/assets/audio/out.wav"
        ], cwd="../UnitSpeech/")
    print("***VOICE CONVERTED***")
    empty_cache()

    return summary

if __name__ == "__main__":
    text = 'نضال حسن واعترف نضال حسن، الذي يدافع عن نفسه، بقتل الجنود، متحججا بحماية المسلمين وعناصر طالبان في أفغانستان، ولكن القاضي العسكري رفض حجته "بحماية الآخرين". وإذا أدين حسن، البالغ من العمر 42 عاما، بقتل 13 شخصا وجرح آخرين فإنه سيواجه عقوبة الإعدام. ويعتبر الحادث الأكثر دموية من بين الهجمات غير القتالية التي وقعت في قاعدة عسكرية أمريكية. وقال شهود عيان دخل في 5 نوفمبر/تشرين الثاني عام 2009 مصحة تعج بالجنود الذين كانوا ينتظرون أدوارهم إجراء فحوصات طبية أو التلقيح، ثم صعد على مكتب، وأطلق النار من سلاحين بيديه، دون توقف إلا لإعادة تعبئة السلاح. مواضيع قد تهمك نهاية وسيقدم ممثلو الادعاء أدلة تفيد بأن حسن مال إلى الأفكار المتطرفة، وكان يزور المواقع بحثا عن ّالجهاديين" وطالبان، ساعات قبل الهجوم. وكان الرائد حسن سيلتحق بالقوات الأمريكية في أفغانستان قبل أن ينفذ هجومه. "عنف في مكان العمل" وصنفت وزارة الدفاع الأمريكية الحادث باعتباره "عنفا في مكان العمل" بدلا من تصنيفه "عملا إرهابيا"، وهو ما أغضب عئلات الضحايا، حسب ما أفاد به مراسل بي بي سي، نك براينت، في فروت هود. ويتوقع أن يدلي العديد من جرحى الحادث بشاهاداتهم أمام المحكمة. وسيواجه حسن عددا من ضحاياه في قاعة المحكمة لأنه سيتولى الدفاع عن نفسه. وهو يستخدم كرسيا متحركا لأنه أصيب بالشلل، عندما أطلق عليه شرطي في القاعدة العسكرية النار.'
    voice = "Saeed"
    print(get_voice(text, voice))