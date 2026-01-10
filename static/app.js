document.addEventListener("DOMContentLoaded", () => {
    const overlay = document.getElementById("age-overlay");
    const appDiv = document.querySelector(".app");
    const confirmBtn = document.getElementById("age-confirm-btn");

    confirmBtn.onclick = () => {
        overlay.style.display = "none";
        appDiv.style.display = "";
    };
});


/*const wsProtocol = location.protocol === "https:" ? "wss" : "ws";
const ws = new WebSocket(`${wsProtocol}://${window.location.host}/ws`);

const localVideo = document.getElementById("localVideo");
const remoteVideo = document.getElementById("remoteVideo");
const startButton = document.getElementById("startBtn");
const callButton = document.getElementById("nextBtn");


const constraints = {
    video: {
        facingMode: "user",
        width: { ideal: 720 },

        height: { ideal: 1280 }
},
    audio: true
};

navigator.mediaDevices.getUserMedia(constraints)


let pc;
let localStream;

const iceConfig = {
    iceServers: [
        { urls: "stun:stun.l.google.com:19302" }
    ]
};

async function initMedia() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });

    localVideo.srcObject = localStream;
}

function createPeer() {
    pc = new RTCPeerConnection(iceConfig);
    localStream.getTracks().forEach(track => { pc.addTrack(track, localStream);
    });

    pc.ontrack = e => {
        remoteVideo.srcObject = e.streams[0];
    };
    pc.onicecandidate = e => {
        if (e.candidate) {
            ws.send(JSON.stringify({ type: "ice", candidate: e.candidate }));
        }
};
}

ws.onmessage = async (event) => {
    const msg = JSON.parse(event.data);

    if (msg.type === "offer") {
        await 
        pc.setRemoteDescription(msg.offer);
        const answer = await pc.createAnswer();
        await pc.setLocalDescription(answer);
        ws.send(JSON.stringify({ type: "answer", answer
        }));
    }

    if (msg.type === "answer") {
        await pc.setRemoteDescription(msg.answer);
    }
    if (msg.type === "ice") {
        await pc.addIceCandidate(msg.candidate);
    }
    if (msg.type === "matched"){
        await initMedia();
        createPeer();

        if (msg.role === "offer"){
            const offer = await pc.createOffer();
            await pc.setLocalDescription(offer);

            ws.send(JSON.stringify({
                type: "offer",
                offer

            }));
        }
        return;
    }
    
};

startButton.onclick = async () => {
    await initMedia();
    createPeer();

        ws.onopen = async () => {
        const offer = await pc.createOffer();
        await pc.setLocalDescription(offer);
        ws.send(JSON.stringify({ type: "offer", offer }));
    };

    // If ws is already open
    if (ws.readyState === WebSocket.OPEN) {
        const offer = await pc.createOffer();
        await pc.setLocalDescription(offer);
        ws.send(JSON.stringify({ type: "offer", offer }));
    }
};

callButton.onclick = () => {
    if (pc) pc.close();
    remoteVideo.srcObject = null;
};


function nextUser() {
    if (pc) {
        pc.ontrack = null;
        pc.onicecandidate = null;
        pc.close();
        pc = null;
    }
    remoteVideo.srcObject = null;
    ws.send(JSON.stringify({ type: "next" }));

    createPeer();
    pc.createOffer().then(offer => pc.setLocalDescription(offer)).then(() => {
        ws.send(JSON.stringify({
            type: "offer",
            offer: pc.localDescription
        }));
        });
    }
callButton.onclick = () => {
    nextUser();
}

let startY = 0;
let endY = 0;

document.addEventListener("touchstart", e => {
    startY = e.touches[0].clientY;
});

document.addEventListener("touchend", e => {
    endY = e.changedTouches[0].clientY;
    if (startY - endY > 80) {
        nextUser();
    }
});*/
