# PyTest Dekoratörler

Pytest , PyPy projesinden kaynaklanan bir Python test çerçevesidir .
Birim testleri , entegrasyon testleri , uçtan uca testler ve işlevsel testler dahil olmak üzere çeşitli yazılım testleri yazmak için kullanılabilir .
Özellikleri, parametreli test, fikstürler ve yeniden yazma iddiasını içerir.

Pytest'te kullanılan bazı dekoratörler:

**@Pytest.fixture()** --> Fonksiyonlarda dönüş değerinin, imzalarında dekore edilmiş fonksiyon adı bulunan test fonksiyonlarına enjekte edilmesini mümkün kılar.

**@pytest.mark.parametrize()** --> Bu dekoratör her yinelemede girilen parametreleri değiştirerek bir test işlevini birden çok kez çağırmaya izin verir.

**@pytest.mark.skip()** --> Bu dekoratör bir test fonksiyonunda belirlenen testi atlamak için kullanılır.

**@pytest.mark.skipİf()** --> Bir test fonksiyonunda verilen koşul True ise testi atlamamızı sağlar.

**@pytest.mark.xfail()** --> Bir testin başarısız olmasını beklediğimizi belirtmek için kullanılır.

**@pytest.mark.timeout()** --> Bir testin belirli bir sürede tamamlanması gerektiğini belirlemek için kullanılır.

**@pytest.mark.dependency()** --> Bu dekoratör testler arası bağımlılıkları belirlemek için kullanılır.
