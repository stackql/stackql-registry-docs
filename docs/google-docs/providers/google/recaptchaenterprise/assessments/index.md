---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
  - recaptchaenterprise
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>assessments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.assessments" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an Assessment of the likelihood an event is legitimate. |
| <CopyableCode code="annotate" /> | `EXEC` | <CopyableCode code="assessmentsId, projectsId" /> | Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fraudulent. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.recaptchaenterprise.assessments (
projectsId,
assessmentEnvironment,
accountVerification,
event,
privatePasswordLeakVerification
)
SELECT 
'{{ projectsId }}',
'{{ assessmentEnvironment }}',
'{{ accountVerification }}',
'{{ event }}',
'{{ privatePasswordLeakVerification }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
phoneFraudAssessment:
  smsTollFraudVerdict:
    reasons:
      - enum: string
        enumDescriptions: string
        type: string
    risk: number
name: string
assessmentEnvironment:
  version: string
  client: string
accountVerification:
  latestVerificationResult: string
  languageCode: string
  endpoints:
    - emailAddress: string
      requestToken: string
      phoneNumber: string
      lastVerificationTime: string
  username: string
tokenProperties:
  hostname: string
  valid: boolean
  invalidReason: string
  androidPackageName: string
  createTime: string
  action: string
  iosBundleId: string
event:
  userIpAddress: string
  fraudPrevention: string
  wafTokenAssessment: boolean
  requestedUri: string
  userAgent: string
  expectedAction: string
  token: string
  hashedAccountId: string
  firewallPolicyEvaluation: boolean
  express: boolean
  headers:
    - type: string
  ja3: string
  siteKey: string
  transactionData:
    billingAddress:
      recipient: string
      address:
        - type: string
      postalCode: string
      regionCode: string
      administrativeArea: string
      locality: string
    user:
      phoneNumber: string
      emailVerified: boolean
      email: string
      accountId: string
      creationMs: string
      phoneVerified: boolean
    paymentMethod: string
    cardBin: string
    items:
      - value: number
        quantity: string
        merchantAccountId: string
        name: string
    currencyCode: string
    gatewayInfo:
      avsResponseCode: string
      name: string
      gatewayResponseCode: string
      cvvResponseCode: string
    transactionId: string
    shippingValue: number
    cardLastFour: string
    value: number
    merchants:
      - phoneNumber: string
        emailVerified: boolean
        email: string
        accountId: string
        creationMs: string
        phoneVerified: boolean
  userInfo:
    userIds:
      - email: string
        username: string
        phoneNumber: string
    createAccountTime: string
    accountId: string
firewallPolicyAssessment:
  error:
    message: string
    code: integer
    details:
      - additionalProperties: any
        type: string
  firewallPolicy:
    description: string
    actions:
      - allow: {}
        substitute:
          path: string
        setHeader:
          value: string
          key: string
        includeRecaptchaScript: {}
        block: {}
        redirect: {}
    path: string
    condition: string
    name: string
privatePasswordLeakVerification:
  encryptedLeakMatchPrefixes:
    - type: string
      format: string
  reencryptedUserCredentialsHash: string
  lookupHashPrefix: string
  encryptedUserCredentialsHash: string
fraudSignals:
  cardSignals:
    cardLabels:
      - type: string
        enum: string
        enumDescriptions: string
  userSignals:
    activeDaysLowerBound: integer
    syntheticRisk: number
riskAnalysis:
  reasons:
    - enum: string
      enumDescriptions: string
      type: string
  extendedVerdictReasons:
    - type: string
  score: number
accountDefenderAssessment:
  labels:
    - enumDescriptions: string
      type: string
      enum: string
fraudPreventionAssessment:
  stolenInstrumentVerdict:
    risk: number
  transactionRisk: number
  cardTestingVerdict:
    risk: number
  behavioralTrustVerdict:
    trust: number

```
</TabItem>
</Tabs>
