#!/usr/bin/env python3
from diavlos.src.organization import Organization

ILLEGAL_ORGS_MAP = {
    'ΕΝΙΑΙΟΣ ΔΙΟΙΚΗΤΙΚΟΣ ΤΟΜΕΑΣ ΘΕΜΑΤΩΝ ΕΚΠΑΙΔΕΥΤΙΚΟΥ ΣΧΕΔΙΑΣΜΟΥ, ΕΚΠΑΙΔΕΥΣΗΣ ΕΛΛΗΝΟΠΑΙΔΩΝ ΤΟΥ ΕΞΩΤΕΡΙΚΟΥ, ΔΙΑΠΟΛΙΤΙΣΤΙΚΗΣ ΕΚΠΑΙΔΕΥΣΗΣ ΚΑΙ ΑΠΟΚΕΝΤΡΩΣΗΣ ΣΤΟ ΥΠ. ΠΑΙΔΕΙΑΣ ΔΙΑ ΒΙΟΥ ΜΑΘΗΣΗΣ ΚΑΙ ΘΡΗΣΚΕΥΜΑΤΩΝ (ΕΙΔΙΚΗ ΓΡΑΜΜΑΤΕΙΑ)':
        'ΔΙΟΙΚΗΤΙΚΟΣ ΤΟΜΕΑΣ ΘΕΜΑΤΩΝ ΕΚΠΑΙΔΕΥΣΗΣ ΕΛΛΗΝΟΠΑΙΔΩΝ ΤΟΥ ΕΞΩΤΕΡΙΚΟΥ ΔΙΑΠΟΛΙΤΙΣΤΙΚΗΣ ΕΚΠΑΙΔΕΥΣΗΣ ΚΑΙ ΑΠΟΚΕΝΤΡΩΣΗΣ ΣΤΟ ΥΠ. ΠΑΙΔΕΙΑΣ',
    'ΑΝΩΝΥΜΗ ΕΤΑΙΡΕΙΑ ΑΞΙΟΠΟΙΗΣΗΣ ΕΥΡΩΠΑΙΚΩΝ ΠΡΟΓΡΑΜΜΑΤΩΝ, ΚΑΤΑΡΤΗΣΗΣ ΥΠΗΡΕΣΙΩΝ ΤΕΧΝΙΚΟΥ ΣΥΜΒΟΥΛΙΟΥ, ΠΕΡΙΒΑΛΛΟΝΤΟΣ ΚΑΙ ΠΟΛΙΤΙΣΜΟΥ ΔΗΜΟΥ ΔΙΟΝΥΣΟΥ':
        'ΑΝΩΝΥΜΗ ΕΤΑΙΡΕΙΑ ΑΞΙΟΠΟΙΗΣΗΣ ΕΥΡΩΠΑΙΚΩΝ ΠΡΟΓΡΑΜΜΑΤΩΝ ΚΑΤΑΡΤΙΣΗΣ ΥΠΗΡΕΣΙΩΝ ΤΕΧΝΙΚΟΥ ΣΥΜΒΟΥΛΙΟΥ, ΠΕΡΙΒ. & ΠΟΛΙΤ. ΔΙΟΝΥΣΟΥ',
    'ΝΟΜΙΚΟ ΠΡΟΣΩΠΟ ΔΗΜΟΣΙΟΥ ΔΙΚΑΙΟΥ ΠΑΙΔΕΙΑΣ ΚΑΙ ΚΟΙΝΩΝΙΚΗΣ ΑΛΛΗΛΕΓΓΥΗΣ - ΠΟΛΙΤΙΣΜΟΥ ΑΘΛΗΤΙΣΜΟΥ ΚΑΙ ΠΕΡΙΒΑΛΛΟΝΤΟΣ ΔΗΜΟΥ ΞΥΛΟΚΑΣΤΡΟΥ-ΕΥΡΩΣΤΙΝΗΣ <<ΗΛΙΑΣ ΚΑΤΣΟΥΛΗΣ>>':
        'ΝΠΔΔ ΠΑΙΔΕΙΑΣ ΚΑΙ ΚΟΙΝΩΝΙΚΗΣ ΑΛΛΗΛΕΓΓΥΗΣ - ΠΟΛΙΤΙΣΜΟΥ ΑΘΛΗΤΙΣΜΟΥ & ΠΕΡΙΒΑΛ. ΔΗΜΟΥ ΞΥΛΟΚΑΣΤΡΟΥ-ΕΥΡΩΣΤΙΝΗΣ Η. ΚΑΤΣΟΥΛΗΣ',
    'ΔΗΜΟΣΥΝΕΤΑΙΡΙΣΤΙΚΗ ΕΤΑΙΡΙΑ ΨΥΚΤΙΚΗΣ ΠΡΟΣΤΑΣΙΑΣ - ΕΜΠΟΡΙΑΣ ΚΑΙ ΔΙΑΚΙΝΗΣΗΣ ΤΩΝ ΑΓΡΟΤΙΚΩΝ ΠΡΟΪΟΝΤΩΝ ΦΥΤΙΚΗΣ ΚΑΙ ΖΩΪΚΗΣ ΠΡΟΕΛΕΥΣΗΣ Ν. ΛΕΣΒΟΥ Α.Ε. (ΔΗΜΟΣΥΝΕΤΑΙΡΙΣΤΙΚΗ ΑΓΡΟΤΙΚΗ Α.Ε.)':
        'ΕΤΑΙΡΙΑ ΨΥΚΤΙΚΗΣ ΠΡΟΣΤΑΣΙΑΣ - ΕΜΠΟΡΙΑΣ & ΔΙΑΚ. ΑΓΡ. ΠΡΟΪΟΝ. ΦΥΤΙΚΗΣ & ΖΩΪΚΗΣ ΠΡΟΕΛΕΥΣΗΣ Ν. ΛΕΣΒΟΥ Α.Ε. ΔΗΜΟΣΥΝΕΤΑΙΡΙΣΤΙΚΗ ΑΓΡΟΤΙΚΗ',
    'ΚΟΙΝΩΦΕΛΗΣ ΔΗΜΟΤΙΚΗ ΕΠΙΧΕΙΡΗΣΗ ΠΟΛΙΤΙΣΜΟΥ, ΑΘΛΗΤΙΣΜΟΥ, ΠΑΙΔΕΙΑΣ, ΚΟΙΝΩΝΙΚΗΣ ΠΡΟΣΤΑΣΙΑΣ ΚΑΙ ΑΛΛΗΛΕΓΓΥΗΣ, ΠΕΡΙΒΑΛΛΟΝΤΟΣ, ΔΗΜΟΤΙΚΗΣ ΣΥΓΚΟΙΝΩΝΙΑΣ, ΕΚΠΟΝΗΣΗΣ ΚΑΙ ΕΦΑΡΜΟΓΗΣ ΠΡΟΓΡΑΜΜΑΤΩΝ ΕΡΕΥΝΑΣ ΚΑΙ ΤΕΧΝΟΛΟΓΙΑΣ ΚΑΙΣΑΡΙΑΝΗΣ':
        'ΚΟΙΝΟΦΕΛΗΣ Δ.Ε. ΠΟΛ., ΑΘΛ., ΠΑΙΔΕΙΑΣ, ΠΡΟΣΤΑΣΙΑΣ & ΑΛΛΗΛΕΓΓΥΗΣ, ΠΕΡΙΒ., ΣΥΓΚ., ΕΚΠΟΝΗΣΗΣ ΚΑΙ ΕΦΑΡΜΟΓΗΣ ΠΡΟΓΡΑΜΜΑΤΩΝ ΕΡΕΥΝΑΣ & ΤΕΧΝ. ΚΑΙΣΑΡΙΑΝΗΣ',
    'ΦΟΡΕΑΣ ΔΙΑΧΕΙΡΙΣΗΣ ΜΗΤΡΟΠΟΛΙΤΙΚΟΥ ΠΑΡΚΟΥ ΠΕΡΙΒΑΛΛΟΝΤΙΚΩΝ ΚΑΙ ΕΚΠΑΙΔΕΥΤΙΚΩΝ ΔΡΑΣΤΗΡΙΟΤΗΤΩΝ ΚΑΙ ΑΝΑΠΤΥΞΗΣ ΚΟΙΝΩΝΙΚΗΣ ΟΙΚΟΝΟΜΙΑΣ "ΑΝΤΩΝΗΣ ΤΡΙΤΣΗΣ"':
        "ΦΟΡΕΑΣ ΔΙΑΧ/ΣΗΣ ΜΗΤΡ. ΠΑΡΚΟΥ ΠΕΡΙΒΑΛΛΟΝΤΙΚΩΝ & ΕΚΠΑΙΔΕΥΤΙΚΩΝ ΔΡΑΣΤΗΡΙΟΤΗΤΩΝ & ΑΝΑΠΤΥΞΗΣ ΚΟΙΝΩΝΙΚΗΣ ΟΙΚΟΝΟΜΙΑΣ 'Α.ΤΡΙΤΣΗΣ'"
}

org = Organization()
illegal_orgs = ILLEGAL_ORGS_MAP.keys()
illegal_orgs_num = len(illegal_orgs)
orgs_details = {
    ILLEGAL_ORGS_MAP[org_name]: org_details
    for org_name, org_details in org.fetch_details_from_api(
        org_names=illegal_orgs).items()
}
org.update_pages(details=orgs_details, force_create=True)
