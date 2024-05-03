---
title: mysql_instances_ssl
hide_title: false
hide_table_of_contents: false
keywords:
  - mysql_instances_ssl
  - databases
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
<tr><td><b>Name</b></td><td><code>mysql_instances_ssl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.mysql_instances_ssl" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDatabasesMySQLInstanceSSL" /> | `SELECT` | <CopyableCode code="instanceId" /> |
| <CopyableCode code="_getDatabasesMySQLInstanceSSL" /> | `EXEC` | <CopyableCode code="instanceId" /> |
