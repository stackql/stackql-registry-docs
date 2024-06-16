---
title: dps_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - dps_certificate
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>dps_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.dps_certificate" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The name of the certificate. |
| <CopyableCode code="etag" /> | `string` | The entity tag. |
| <CopyableCode code="properties" /> | `object` | The description of an X509 CA Certificate. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Get the certificate from the provisioning service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, provisioningServiceName, resourceGroupName, subscriptionId" /> | Get all the certificates tied to the provisioning service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Add new certificate or update an existing certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Deletes the specified certificate associated with the Provisioning Service |
| <CopyableCode code="generate_verification_code" /> | `EXEC` | <CopyableCode code="If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Generate verification code for Proof of Possession. |
| <CopyableCode code="verify_certificate" /> | `EXEC` | <CopyableCode code="If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |
