---
title: firewall_domain_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_domain_lists
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>firewall_domain_list</code> resource or lists <code>firewall_domain_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_domain_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::FirewallDomainList.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.firewall_domain_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>FirewallDomainListName</td></tr>
<tr><td><CopyableCode code="domain_count" /></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><CopyableCode code="managed_owner_name" /></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="modification_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><CopyableCode code="domains" /></td><td><code>array</code></td><td>An inline list of domains to use for this domain list.</td></tr>
<tr><td><CopyableCode code="domain_file_url" /></td><td><code>string</code></td><td>S3 URL to import domains from.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>firewall_domain_lists</code> in a region.
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
FROM aws.route53resolver.firewall_domain_lists
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>firewall_domain_list</code>.
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
FROM aws.route53resolver.firewall_domain_lists
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_domain_list</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.route53resolver.firewall_domain_lists (
 Name,
 Domains,
 DomainFileUrl,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ Domains }}',
 '{{ DomainFileUrl }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.firewall_domain_lists (
 Name,
 Domains,
 DomainFileUrl,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Domains }}',
 '{{ DomainFileUrl }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: firewall_domain_list
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Domains
        value:
          - '{{ Domains[0] }}'
      - name: DomainFileUrl
        value: '{{ DomainFileUrl }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.firewall_domain_lists
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>firewall_domain_lists</code> resource, the following permissions are required:

### Create
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

### List
```json
route53resolver:*,
ec2:*,
logs:*,
iam:*,
lambda:*,
s3:*
```

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

