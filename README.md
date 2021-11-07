            var positions = [
            {
                title: '카카오',
                content: '<div>카카오</div>',
                latlng: new kakao.maps.LatLng(33.450705, 126.570677)
            },
            {
                title: '생태연못',
                content: '<div>생태연못</div>',
                latlng: new kakao.maps.LatLng(33.450936, 126.569477)
            },
            {
                title: '텃밭',
                content: '<div>텃밭</div>',
                latlng: new kakao.maps.LatLng(33.450879, 126.569940)
            },
            {
                title: '근린공원',
                content: '<div>근린공원</div>',
                latlng: new kakao.maps.LatLng(33.451393, 126.570738)
            }
        ];
    //   식으로 저장된 것을
      // 지도 표기해줌
       //latlng: new kakao.maps.LatLng(33.451393, 126.570738) 은 위도 경도 인데.
       
            // 주소-좌표 변환 객체를 생성합니다
            var geocoder = new kakao.maps.services.Geocoder();

            // 주소로 좌표를 검색합니다
            geocoder.addressSearch('제주특별자치도 제주시 첨단로 242', function(result, status) {

            // 정상적으로 검색이 완료됐으면 
            if (status === kakao.maps.services.Status.OK) {
            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 결과값으로 받은 위치를 마커로 표시합니다
            var marker = new kakao.maps.Marker({
            map: map,
            position: coords
            });

            // 인포윈도우로 장소에 대한 설명을 표시합니다
            var infowindow = new kakao.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:6px 0;">우리회사</div>'
            });
            infowindow.open(map, marker);

            // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
            map.setCenter(coords);
            } 
            });    
사용하면 주소르 위도/경도로 바꿀수 있을듯!

https://apis.map.kakao.com/web/sample/addr2coord/
