import type { Metadata } from "next";
import { Literata, Source_Sans_3 } from "next/font/google";
import { BookShell } from "@/components/BookShell";
import { FRONT_PAGES, getSections } from "@/lib/content";
import "./globals.css";

const book = Literata({
  subsets: ["latin"],
  variable: "--font-book",
  display: "swap",
});

const ui = Source_Sans_3({
  subsets: ["latin"],
  variable: "--font-ui",
  display: "swap",
});

export const metadata: Metadata = {
  title: "GRE Mathematics Book — 1036 Skills to a Perfect Score",
  description:
    "A complete course through every atomic skill on the GRE Mathematics Subject Test, taught from first principles.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const sections = getSections();
  return (
    <html lang="en">
      <body className={`${book.variable} ${ui.variable} font-sans antialiased`}>
        <BookShell sections={sections} front={FRONT_PAGES}>
          {children}
        </BookShell>
      </body>
    </html>
  );
}
