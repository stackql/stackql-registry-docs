---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
  - transfer_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer_api.public_keys" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="import_public_key" /> | `INSERT` | <CopyableCode code="data__ServerId, data__SshPublicKeyBody, data__UserName, region" /> | &lt;p&gt;Adds a Secure Shell (SSH) public key to a Transfer Family user identified by a &lt;code&gt;UserName&lt;/code&gt; value assigned to the specific file transfer protocol-enabled server, identified by &lt;code&gt;ServerId&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The response returns the &lt;code&gt;UserName&lt;/code&gt; value, the &lt;code&gt;ServerId&lt;/code&gt; value, and the name of the &lt;code&gt;SshPublicKeyId&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="delete_public_key" /> | `DELETE` | <CopyableCode code="data__ServerId, data__SshPublicKeyId, data__UserName, region" /> | Deletes a user's Secure Shell (SSH) public key. |
