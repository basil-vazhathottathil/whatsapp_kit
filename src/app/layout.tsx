import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "whatsapp_kit",
  description: "idk how this worked ",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
