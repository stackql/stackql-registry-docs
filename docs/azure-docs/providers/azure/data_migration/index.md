---
title: data_migration
hide_title: false
hide_table_of_contents: false
keywords:
  - data_migration
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
The Database Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customers virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure.data_migration</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>Azure Database Migration Service Resource Provider (Microsoft.DataMigration)</td></tr>
<tr><td><b>Description</b></td><td>The Database Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customers virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.</td></tr>
<tr><td><b>Id</b></td><td><code>data_migration:v0.3.0</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/data_migration/database_migrations_sql_db/">database_migrations_sql_db</a><br />
<a href="/providers/azure/data_migration/database_migrations_sql_mi/">database_migrations_sql_mi</a><br />
<a href="/providers/azure/data_migration/database_migrations_sql_vm/">database_migrations_sql_vm</a><br />
<a href="/providers/azure/data_migration/files/">files</a><br />
<a href="/providers/azure/data_migration/operations/">operations</a><br />
<a href="/providers/azure/data_migration/projects/">projects</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/data_migration/resource_skus/">resource_skus</a><br />
<a href="/providers/azure/data_migration/service_tasks/">service_tasks</a><br />
<a href="/providers/azure/data_migration/services/">services</a><br />
<a href="/providers/azure/data_migration/sql_migration_services/">sql_migration_services</a><br />
<a href="/providers/azure/data_migration/tasks/">tasks</a><br />
<a href="/providers/azure/data_migration/usages/">usages</a><br />
</div>
</div>
