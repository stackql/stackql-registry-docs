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
accountVerification,
event,
assessmentEnvironment,
privatePasswordLeakVerification
)
SELECT 
'{{ projectsId }}',
'{{ accountVerification }}',
'{{ event }}',
'{{ assessmentEnvironment }}',
'{{ privatePasswordLeakVerification }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: accountVerification
      value:
        - name: username
          value: '{{ username }}'
        - name: languageCode
          value: '{{ languageCode }}'
        - name: endpoints
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: event
      value:
        - name: ja3
          value: '{{ ja3 }}'
        - name: expectedAction
          value: '{{ expectedAction }}'
        - name: hashedAccountId
          value: '{{ hashedAccountId }}'
        - name: fraudPrevention
          value: '{{ fraudPrevention }}'
        - name: wafTokenAssessment
          value: '{{ wafTokenAssessment }}'
        - name: express
          value: '{{ express }}'
        - name: firewallPolicyEvaluation
          value: '{{ firewallPolicyEvaluation }}'
        - name: userAgent
          value: '{{ userAgent }}'
        - name: transactionData
          value:
            - name: value
              value: '{{ value }}'
            - name: currencyCode
              value: '{{ currencyCode }}'
            - name: merchants
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: transactionId
              value: '{{ transactionId }}'
            - name: cardBin
              value: '{{ cardBin }}'
            - name: billingAddress
              value:
                - name: address
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: administrativeArea
                  value: '{{ administrativeArea }}'
                - name: recipient
                  value: '{{ recipient }}'
                - name: postalCode
                  value: '{{ postalCode }}'
                - name: locality
                  value: '{{ locality }}'
                - name: regionCode
                  value: '{{ regionCode }}'
            - name: user
              value:
                - name: emailVerified
                  value: '{{ emailVerified }}'
                - name: phoneNumber
                  value: '{{ phoneNumber }}'
                - name: email
                  value: '{{ email }}'
                - name: creationMs
                  value: '{{ creationMs }}'
                - name: accountId
                  value: '{{ accountId }}'
                - name: phoneVerified
                  value: '{{ phoneVerified }}'
            - name: paymentMethod
              value: '{{ paymentMethod }}'
            - name: cardLastFour
              value: '{{ cardLastFour }}'
            - name: items
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: shippingValue
              value: '{{ shippingValue }}'
            - name: gatewayInfo
              value:
                - name: name
                  value: '{{ name }}'
                - name: cvvResponseCode
                  value: '{{ cvvResponseCode }}'
                - name: avsResponseCode
                  value: '{{ avsResponseCode }}'
                - name: gatewayResponseCode
                  value: '{{ gatewayResponseCode }}'
        - name: userInfo
          value:
            - name: userIds
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: accountId
              value: '{{ accountId }}'
            - name: createAccountTime
              value: '{{ createAccountTime }}'
        - name: userIpAddress
          value: '{{ userIpAddress }}'
        - name: siteKey
          value: '{{ siteKey }}'
        - name: token
          value: '{{ token }}'
        - name: headers
          value:
            - name: type
              value: '{{ type }}'
        - name: requestedUri
          value: '{{ requestedUri }}'
    - name: assessmentEnvironment
      value:
        - name: version
          value: '{{ version }}'
        - name: client
          value: '{{ client }}'
    - name: privatePasswordLeakVerification
      value:
        - name: lookupHashPrefix
          value: '{{ lookupHashPrefix }}'
        - name: encryptedUserCredentialsHash
          value: '{{ encryptedUserCredentialsHash }}'

```
</TabItem>
</Tabs>
