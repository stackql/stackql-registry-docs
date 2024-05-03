---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This keypair's unique ID |
| <CopyableCode code="access_key" /> | `string` | This keypair's access key. This is not secret. |
| <CopyableCode code="bucket_access" /> | `array` | Defines this key as a Limited Access Key. Limited Access Keys restrict this Object Storage key's access to only the bucket(s) declared in this array and define their bucket-level permissions.<br /><br /><br />  Limited Access Keys can:<br /><br />  * [list all buckets](/docs/api/object-storage/#object-storage-buckets-list) available on this Account, but cannot perform any actions on a bucket unless it has access to the bucket.<br /><br /><br />  * [create new buckets](/docs/api/object-storage/#object-storage-bucket-create), but do not have any access to the buckets it creates, unless explicitly given access to them.<br /><br /><br />  **Note:** You can create an Object Storage Limited Access Key without access to any buckets.<br />  This is achieved by sending a request with an empty `bucket_access` array.<br /><br /><br />  **Note:** If this field is omitted, a regular unlimited access key is issued.<br /> |
| <CopyableCode code="label" /> | `string` | The label given to this key. For display purposes only. |
| <CopyableCode code="limited" /> | `boolean` | Whether or not this key is a limited access key. Will return `false` if this key grants full access to all buckets on the user's account. |
| <CopyableCode code="secret_key" /> | `string` | This keypair's secret key. Only returned on key creation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getObjectStorageKey" /> | `SELECT` | <CopyableCode code="keyId" /> | Returns a single Object Storage Key provisioned for your account.<br /> |
| <CopyableCode code="getObjectStorageKeys" /> | `SELECT` |  | Returns a paginated list of Object Storage Keys for authenticating to<br />the Object Storage S3 API.<br /> |
| <CopyableCode code="createObjectStorageKeys" /> | `INSERT` |  | Provisions a new Object Storage Key on your account.<br /><br />Accounts with negative balances cannot access this command.<br /><br />* To create a Limited Access Key with specific permissions, send a `bucket_access` array.<br /><br />* To create a Limited Access Key without access to any buckets, send an empty `bucket_access` array.<br /><br />* To create an Access Key with unlimited access to all clusters and all buckets, omit the `bucket_access` array.<br /> |
| <CopyableCode code="deleteObjectStorageKey" /> | `DELETE` | <CopyableCode code="keyId" /> | Revokes an Object Storage Key.  This keypair will no longer be usable by third-party clients.<br /> |
| <CopyableCode code="_getObjectStorageKey" /> | `EXEC` | <CopyableCode code="keyId" /> | Returns a single Object Storage Key provisioned for your account.<br /> |
| <CopyableCode code="_getObjectStorageKeys" /> | `EXEC` |  | Returns a paginated list of Object Storage Keys for authenticating to<br />the Object Storage S3 API.<br /> |
| <CopyableCode code="updateObjectStorageKey" /> | `EXEC` | <CopyableCode code="keyId" /> | Updates an Object Storage Key on your account.<br /> |
