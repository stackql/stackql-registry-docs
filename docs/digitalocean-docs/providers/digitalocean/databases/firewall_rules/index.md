---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - databases
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.firewall_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_uuid" /> | `string` | A unique ID for the database cluster to which the rule is applied. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the firewall rule was created. |
| <CopyableCode code="type" /> | `string` | The type of resource that the firewall rule allows to access the database cluster. |
| <CopyableCode code="uuid" /> | `string` | A unique ID for the firewall rule itself. |
| <CopyableCode code="value" /> | `string` | The ID of the specific resource, the name of a tag applied to a group of resources, or the IP address that the firewall rule allows to access the database cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_firewall_rules" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of a database cluster's firewall rules (known as "trusted sources" in the control panel), send a GET request to `/v2/databases/$DATABASE_ID/firewall`.<br />The result will be a JSON object with a `rules` key. |
| <CopyableCode code="_list_firewall_rules" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To list all of a database cluster's firewall rules (known as "trusted sources" in the control panel), send a GET request to `/v2/databases/$DATABASE_ID/firewall`.<br />The result will be a JSON object with a `rules` key. |
| <CopyableCode code="update_firewall_rules" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To update a database cluster's firewall rules (known as "trusted sources" in the control panel), send a PUT request to `/v2/databases/$DATABASE_ID/firewall` specifying which resources should be able to open connections to the database. You may limit connections to specific Droplets, Kubernetes clusters, or IP addresses. When a tag is provided, any Droplet or Kubernetes node with that tag applied to it will have access. The firewall is limited to 100 rules (or trusted sources). When possible, we recommend [placing your databases into a VPC network](https://www.digitalocean.com/docs/networking/vpc/) to limit access to them instead of using a firewall.<br />A successful |
