---
title: certificate_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders
  - app_service
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

Creates, updates, deletes, gets or lists a <code>certificate_orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.certificate_orders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | AppServiceCertificateOrder resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Get a certificate order. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for List all certificate orders in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get certificate orders in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Create or update a certificate purchase order. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Delete an existing certificate order. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Create or update a certificate purchase order. |
| <CopyableCode code="reissue" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Reissue an existing certificate order. |
| <CopyableCode code="renew" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Renew an existing certificate order. |
| <CopyableCode code="resend_email" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Resend certificate email. |
| <CopyableCode code="resend_request_emails" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order |
| <CopyableCode code="retrieve_certificate_actions" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieve the list of certificate actions. |
| <CopyableCode code="retrieve_certificate_email_history" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieve email history. |
| <CopyableCode code="retrieve_site_seal" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times. |
| <CopyableCode code="validate_purchase_information" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Validate information for a certificate order. |
| <CopyableCode code="verify_domain_ownership" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Verify domain ownership for this certificate order. |

## `SELECT` examples

Description for List all certificate orders in a subscription.


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.certificate_orders
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_orders</code> resource.

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
INSERT INTO azure.app_service.certificate_orders (
certificateOrderName,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties
)
SELECT 
'{{ certificateOrderName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: certificates
          value: object
        - name: distinguishedName
          value: string
        - name: domainVerificationToken
          value: string
        - name: validityInYears
          value: integer
        - name: keySize
          value: integer
        - name: productType
          value: string
        - name: autoRenew
          value: boolean
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: signedCertificate
          value:
            - name: version
              value: integer
            - name: serialNumber
              value: string
            - name: thumbprint
              value: string
            - name: subject
              value: string
            - name: notBefore
              value: string
            - name: notAfter
              value: string
            - name: signatureAlgorithm
              value: string
            - name: issuer
              value: string
            - name: rawData
              value: string
        - name: csr
          value: string
        - name: serialNumber
          value: string
        - name: lastCertificateIssuanceTime
          value: string
        - name: expirationTime
          value: string
        - name: isPrivateKeyExternal
          value: boolean
        - name: appServiceCertificateNotRenewableReasons
          value:
            - string
        - name: nextAutoRenewalTimeStamp
          value: string
        - name: contact
          value:
            - name: email
              value: string
            - name: nameFirst
              value: string
            - name: nameLast
              value: string
            - name: phone
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_orders</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.certificate_orders
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
certificateOrderName = '{{ certificateOrderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_orders</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.certificate_orders
WHERE certificateOrderName = '{{ certificateOrderName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
