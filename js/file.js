var firebaseConfig = {
	apiKey: 'xxxxx',
	projectId: 'yyyyy',
	storageBucket: 'gs://md-edit-c7e0a.appspot.com',
  }
  firebase.initializeApp(firebaseConfig);

  //formのsubmitにイベント設定

  var form = document.querySelector('form');
  form.addEventListener('submit', function (e) {
	e.preventDefault();
	
	var imgs = form.querySelector('input');
	var uploads = [];
	for (var file of imgs.files) {

		//選択したファイルのファイル名を使うが、場合によってはかぶるので注意
	  var storageRef = firebase.storage().ref('form-uploaded/' + file.name);
	  uploads.push(storageRef.put(file));
	}

	//すべての画像のアップロード完了を待つ
	Promise.all(uploads).then(function () {
	  console.log('アップロード完了');
	});
  });