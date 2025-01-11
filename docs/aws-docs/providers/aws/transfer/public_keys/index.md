---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
  - transfer
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Imports or deletes a public key for a user

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>public_keys</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.public_keys" /></td></tr>
</tbody></table>

## Fields
<code>SELECT</code> operation not supported for this resource.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="import_public_key" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__ServerId, data__SshPublicKeyBody, data__UserName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_public_key" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__ServerId, data__SshPublicKeyId, data__UserName, region" /></td>
  </tr>
</tbody></table>






