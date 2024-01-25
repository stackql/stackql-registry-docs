---
title: managers_public_encryption_key
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_public_encryption_key
  - storsimple_8000_series
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers_public_encryption_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.managers_public_encryption_key</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `encryptionAlgorithm` | `string` | The algorithm used to encrypt the "Value". |
| `value` | `string` | The value of the secret itself. If the secret is in plaintext or null then EncryptionAlgorithm will be none. |
| `valueCertificateThumbprint` | `string` | The thumbprint of the cert that was used to encrypt "Value". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `managerName, resourceGroupName, subscriptionId` |
