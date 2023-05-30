---
title: open_id_connect_provider_thumbprints
hide_title: false
hide_table_of_contents: false
keywords:
  - open_id_connect_provider_thumbprints
  - iam
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_id_connect_provider_thumbprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.open_id_connect_provider_thumbprints</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `open_id_connect_provider_thumbprints_Update` | `EXEC` | `OpenIDConnectProviderArn, ThumbprintList, region` |
