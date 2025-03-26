import Image from "next/image";
import Card from "./components/card/Card";

export default function Home() {
  return (
    <div className="flex flex-col justify-center items-center min-h-screen"
      style={{backgroundImage: "url('/bg.jpg')"}}>
    <Card/>
    </div>
  );
}
