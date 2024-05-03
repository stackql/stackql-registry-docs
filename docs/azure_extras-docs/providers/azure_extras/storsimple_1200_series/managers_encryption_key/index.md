---
title: managers_encryption_key
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_encryption_key
  - storsimple_1200_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>managers_encryption_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.managers_encryption_key" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryptionAlgorithm" /> | `string` | Algorithm used to encrypt "Value" |
| <CopyableCode code="value" /> | `string` | The value of the secret itself. If the secret is in plaintext or null then EncryptionAlgorithm will be none |
| <CopyableCode code="valueCertificateThumbprint" /> | `string` | Thumbprint cert that was used to encrypt "Value" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> |
