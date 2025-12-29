import React from "react";
import { Card } from "../Components/Ui/export.js";

function TermsOfService() {
    return (
        <div className="max-w-5xl mx-auto px-4 py-10 text-text-primary">

            {/* Page Header */}
            <div className="mb-8">
                <h1 className="text-3xl font-bold mb-2">Terms & Conditions</h1>
                <p className="text-text-secondary">
                    Please read these terms carefully before using PyChat.
                </p>
            </div>

            <div className="space-y-6">

                <Card title="1. Acceptance of Terms">
                    <p className="text-text-secondary">
                        By accessing or using PyChat, you agree to be bound by these Terms
                        and Conditions. If you do not agree, you may not use the platform.
                    </p>
                </Card>

                <Card title="2. Eligibility">
                    <p className="text-text-secondary">
                        You must be at least 13 years old to use PyChat. By using the
                        platform, you confirm that you meet this requirement and are
                        legally capable of entering into this agreement.
                    </p>
                </Card>

                <Card title="3. User Accounts">
                    <p className="text-text-secondary">
                        You are responsible for maintaining the confidentiality of your
                        account credentials and for all activities that occur under your
                        account. PyChat is not responsible for unauthorized access caused
                        by your failure to secure your login information.
                    </p>
                </Card>

                <Card title="4. Acceptable Use Policy">
                    <p className="text-text-secondary mb-3">
                        You agree not to use PyChat for any unlawful or harmful activities,
                        including but not limited to:
                    </p>
                    <ul className="list-disc list-inside space-y-1 text-text-secondary">
                        <li>Sending spam, malware, or phishing content</li>
                        <li>Harassment, abuse, or hate speech</li>
                        <li>Violating the privacy or rights of others</li>
                        <li>Attempting to disrupt or compromise platform security</li>
                    </ul>
                </Card>

                <Card title="5. Message Content & Encryption">
                    <p className="text-text-secondary">
                        PyChat uses end-to-end encryption to protect message content.
                        However, users are solely responsible for the content they share.
                        PyChat does not monitor private conversations but may take action
                        if required by law.
                    </p>
                </Card>

                <Card title="6. Service Availability">
                    <p className="text-text-secondary">
                        We strive to keep PyChat available at all times, but we do not
                        guarantee uninterrupted access. Maintenance, updates, or technical
                        issues may temporarily affect availability.
                    </p>
                </Card>

                <Card title="7. Termination">
                    <p className="text-text-secondary">
                        PyChat reserves the right to suspend or terminate accounts that
                        violate these terms, misuse the platform, or pose a security risk
                        to other users or the service.
                    </p>
                </Card>

                <Card title="8. Limitation of Liability">
                    <p className="text-text-secondary">
                        To the fullest extent permitted by law, PyChat shall not be liable
                        for any indirect, incidental, or consequential damages arising
                        from your use of the platform.
                    </p>
                </Card>

                <Card title="9. Changes to Terms">
                    <p className="text-text-secondary">
                        These Terms may be updated from time to time. Continued use of
                        PyChat after changes are posted constitutes acceptance of the
                        revised terms.
                    </p>
                </Card>

                <Card
                    title="10. Contact Information"
                    footer="Last updated: August 2025"
                >
                    <p className="text-text-secondary">
                        If you have any questions regarding these Terms, please contact us
                        at{" "}
                        <span className="text-accent font-medium">
                            support@pychat.app
                        </span>.
                    </p>
                </Card>

            </div>
        </div>
    );
}

export default TermsOfService;
