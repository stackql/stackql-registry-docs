---
title: sites_services_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_services_instances
  - service_instance
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_services_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.service_instance.sites_services_instances" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="createServiceInstance" /> | `INSERT` | <CopyableCode code="addon, site_id" /> |
| <CopyableCode code="deleteServiceInstance" /> | `DELETE` | <CopyableCode code="addon, instance_id, site_id" /> |
| <CopyableCode code="showServiceInstance" /> | `EXEC` | <CopyableCode code="addon, instance_id, site_id" /> |
| <CopyableCode code="updateServiceInstance" /> | `EXEC` | <CopyableCode code="addon, instance_id, site_id" /> |
