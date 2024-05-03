---
title: buckets_ssl
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_ssl
  - object_storage
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets_ssl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.buckets_ssl" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getObjectStorageSSL" /> | `SELECT` | <CopyableCode code="bucket, clusterId" /> | Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was<br />uploaded by an Account user.<br /> |
| <CopyableCode code="createObjectStorageSSL" /> | `INSERT` | <CopyableCode code="bucket, clusterId, data__certificate, data__private_key" /> | Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS.<br />Your TLS/SSL certificate and private key are stored encrypted at rest.<br /><br /><br />To replace an expired certificate, [delete your current certificate](/docs/api/object-storage/#object-storage-tlsssl-cert-delete)<br />and upload a new one.<br /> |
| <CopyableCode code="deleteObjectStorageSSL" /> | `DELETE` | <CopyableCode code="bucket, clusterId" /> | Deletes this Object Storage bucket's user uploaded TLS/SSL certificate and private key.<br /> |
| <CopyableCode code="_getObjectStorageSSL" /> | `EXEC` | <CopyableCode code="bucket, clusterId" /> | Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was<br />uploaded by an Account user.<br /> |
