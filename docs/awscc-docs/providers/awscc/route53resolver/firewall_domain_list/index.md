---
title: firewall_domain_list
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_domain_list
  - route53resolver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>firewall_domain_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_domain_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_domain_list</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.firewall_domain_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>FirewallDomainListName</td></tr>
<tr><td><code>domain_count</code></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><code>managed_owner_name</code></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><code>creator_request_id</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>modification_time</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>domain_file_url</code></td><td><code>string</code></td><td>S3 URL to import domains from.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
name,
domain_count,
status,
status_message,
managed_owner_name,
creator_request_id,
creation_time,
modification_time,
domains,
domain_file_url,
tags
FROM awscc.route53resolver.firewall_domain_list
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>firewall_domain_list</code> resource, the following permissions are required:

### Read
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

### Delete
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

### Update
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

