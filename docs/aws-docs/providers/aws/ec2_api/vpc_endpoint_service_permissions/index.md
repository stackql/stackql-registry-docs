---
title: vpc_endpoint_service_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_service_permissions
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>vpc_endpoint_service_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_endpoint_service_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="principal" /> | `string` | The Amazon Resource Name (ARN) of the principal. |
| <CopyableCode code="principalType" /> | `string` | The type of principal. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpc_endpoint_service_permissions_Describe" /> | `SELECT` | <CopyableCode code="ServiceId, region" /> | Describes the principals (service consumers) that are permitted to discover your VPC endpoint service. |
| <CopyableCode code="vpc_endpoint_service_permissions_Modify" /> | `EXEC` | <CopyableCode code="ServiceId, region" /> | &lt;p&gt;Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (IAM users, IAM roles, and Amazon Web Services accounts) to connect to your endpoint service.&lt;/p&gt; &lt;p&gt;If you grant permissions to all principals, the service is public. Any users who know the name of a public service can send a request to attach an endpoint. If the service does not require manual approval, attachments are automatically approved.&lt;/p&gt; |
