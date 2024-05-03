---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - iot_hub
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The name of the certificate. |
| <CopyableCode code="etag" /> | `string` | The entity tag. |
| <CopyableCode code="properties" /> | `object` | The description of an X509 CA Certificate. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Returns the certificate. |
| <CopyableCode code="list_by_iot_hub" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Returns the list of certificates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Adds new or replaces existing certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Deletes an existing X509 certificate or does nothing if it does not exist. |
| <CopyableCode code="_list_by_iot_hub" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Returns the list of certificates. |
| <CopyableCode code="generate_verification_code" /> | `EXEC` | <CopyableCode code="If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |
