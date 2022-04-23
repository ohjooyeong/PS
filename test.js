import dateFormat from 'dateformat';

import Jspdf from 'jspdf';
import i18n from 'i18next';
import 'jspdf-autotable';

import fontBold from '../../../fonts/NanumBarunGothic-bold';
import font from '../../../fonts/NanumBarunGothic-normal';
import jpfont from '../../../fonts/GL-AntiquePlus-normal';

let doc;
let date;
let id;

const writeFileName = () => {
  doc.setFillColor(133, 132, 128);
  doc.rect(0, 0, 220, 20, 'F');
  doc.setFontSize(16);
  doc.setTextColor(255);
  doc.setFontSize(14);
  doc.text(
    5,
    17,
    `Date : ${date.toLocaleDateString('en', {
      timeZone: 'UTC',
    })}`,
  );
  doc.setFontSize(10);
  doc.addImage(Aifbms, 'png', 148, 3, 40, 8);
  doc.setTextColor(0);
};

const writeTitle = title => {
  doc.setFontSize(12);
  doc.text(15, (doc.lastAutoTable.finalY || 130) + 10, title);
};

export const createDoc = (newId, canvas) => {
  doc = new Jspdf('p', 'mm', 'a4');
  const lan = i18n.language;
  const fonts = {
    ko: 'NanumBarunGothic',
    jp: 'GL-AntiquePlus',
  };
  const ttf = {
    ko: font,
    jp: jpfont,
  };
  doc.addFileToVFS(`NanumBarunGothicBold.ttf`, fontBold);
  doc.addFont(`NanumBarunGothicBold.ttf`, `NanumBarunGothicBold`, 'bold');
  doc.setFont('NanumBarunGothicBold', 'bold', 'bold');
  id = newId;
  date = new Date();

  const t = target => {
    if (resources[lan]) {
      return resources[lan].translation[target];
    }
    return target;
  };

  writeFileName(lan);
  doc.addFileToVFS(`${fonts[lan]}.ttf`, ttf[lan]);
  doc.addFont(`${fonts[lan]}.ttf`, `${fonts[lan]}`, 'normal');

  writeTitle(t('이벤트'));

  const pages = doc.internal.getNumberOfPages();
  const pageWidth = doc.internal.pageSize.width;
  const pageHeight = doc.internal.pageSize.height;
  const horizontalPos = pageWidth / 2;
  const verticalPos = pageHeight - 10;
  doc.setFontSize(10);
  for (let j = 1; j < pages + 1; j += 1) {
    doc.setPage(j);
    doc.text(`${j} of ${pages}`, horizontalPos, verticalPos, {
      align: 'center',
    });
  }

  return doc;
};

export const saveDoc = () =>
  doc.save(`_${id}_${dateFormat(date, 'yyyymmdd_HHMMss')}.pdf`);
