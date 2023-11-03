---
title: storage_virtual_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_virtual_machine
  - fsx
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>storage_virtual_machine</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_virtual_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.storage_virtual_machine</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceARN</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SvmAdminPassword</code></td><td><code>string</code></td><td></td></tr><tr><td><code>StorageVirtualMachineId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ActiveDirectoryConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RootVolumeSecurityStyle</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FileSystemId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UUID</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.fsx.storage_virtual_machine
WHERE region = 'us-east-1' AND data__Identifier = '{StorageVirtualMachineId}'
```
